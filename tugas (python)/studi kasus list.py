class Pasien:
    def __init__(self, nama, kondisi, urgensi=False):
        self.nama = nama
        self.kondisi = kondisi
        self.urgensi = urgensi
        self.status = "Menunggu"
        self.biaya = 0

class DokterSpesialis:
    def __init__(self, nama, spesialisasi):
        self.nama = nama
        self.spesialisasi = spesialisasi

class SistemInformasiRumahSakit:
    def __init__(self):
        self.antrian_pasien = []
        self.pasien_dipanggil = []
        self.rekap_pasien_hari_ini = []
        self.dokter_spesialis = []

    def ambil_antrian(self, pasien):
        if pasien.urgensi:
            self.antrian_pasien.insert(0, pasien)
            print(f"{pasien.nama} (Urgensi) telah mengambil antrian.")
        else:
            self.antrian_pasien.append(pasien)
            print(f"{pasien.nama} telah mengambil antrian.")

    def panggil_pasien(self):
        if self.antrian_pasien:
            pasien = self.antrian_pasien.pop(0)
            pasien.status = "Dipanggil"
            self.pasien_dipanggil.append(pasien)
            print(f"{pasien.nama} dipanggil untuk pemeriksaan.")
        else:
            print("Tidak ada pasien dalam antrian.")

    def pemeriksaan_dokter(self, pasien, biaya, dokter=None):
        if pasien in self.pasien_dipanggil:
            if dokter:
                print(f"{pasien.nama} diperiksa oleh {dokter.nama} ({dokter.spesialisasi}).")
            if pasien.kondisi.lower() == "rawat jalan":
                pasien.biaya = biaya
                print(f"{pasien.nama} dirawat jalan. Biaya: {biaya}")
            elif pasien.kondisi.lower() == "rawat inap":
                pasien.biaya = biaya
                print(f"{pasien.nama} dirawat inap. Biaya: {biaya}")
            pasien.status = "Selesai"
            self.rekap_pasien_hari_ini.append(pasien)
        else:
            print(f"{pasien.nama} belum dipanggil untuk pemeriksaan.")

    def pembayaran_rawat_inap(self, pasien):
        if pasien.kondisi.lower() == "rawat inap" and pasien.status == "Selesai":
            print(f"{pasien.nama} telah membayar biaya rawat inap sebesar {pasien.biaya}.")
        else:
            print(f"{pasien.nama} tidak memerlukan pembayaran rawat inap atau belum selesai diperiksa.")

    def tampilkan_data_pasien(self, jenis):
        print(f"Data Pasien {jenis}:")
        for pasien in self.rekap_pasien_hari_ini:
            if pasien.kondisi.lower() == jenis.lower():
                print(f"Nama: {pasien.nama}, Kondisi: {pasien.kondisi}, Status: {pasien.status}, Biaya: {pasien.biaya}")

    def tambah_dokter_spesialis(self, dokter):
        self.dokter_spesialis.append(dokter)
        print(f"Dokter {dokter.nama} ({dokter.spesialisasi}) telah ditambahkan.")

# Contoh penggunaan
sistem = SistemInformasiRumahSakit()

# Menambahkan dokter spesialis
dokter1 = DokterSpesialis("Dr. Ahmad", "Kardiologi")
dokter2 = DokterSpesialis("Dr. Siti", "Neurologi")
sistem.tambah_dokter_spesialis(dokter1)
sistem.tambah_dokter_spesialis(dokter2)

# Pasien
pasien1 = Pasien("Budi", "Rawat Jalan")
pasien2 = Pasien("Ani", "Rawat Inap", urgensi=True)
pasien3 = Pasien("Cici", "Rawat Inap")

sistem.ambil_antrian(pasien1)
sistem.ambil_antrian(pasien2)
sistem.ambil_antrian(pasien3)

sistem.panggil_pasien()
sistem.pemeriksaan_dokter(pasien2, 500000, dokter1)

sistem.panggil_pasien()
sistem.pemeriksaan_dokter(pasien1, 150000)

sistem.panggil_pasien()
sistem.pemeriksaan_dokter(pasien3, 750000, dokter2)

sistem.pembayaran_rawat_inap(pasien2)
sistem.pembayaran_rawat_inap(pasien3)

sistem.tampilkan_data_pasien("Rawat Jalan")
sistem.tampilkan_data_pasien("Rawat Inap")