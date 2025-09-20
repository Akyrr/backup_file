# def pembukaan():
#     print('=====================')
#     print('selamat datang di pt sidomakmur')
#     print('=====================')
# pembukaan()


# def pembukaan(namaadmin,namapt):
#     print('=======================')
#     print(f'Selamat datang di PT {namapt}')
#     print('=======================')
#     print(f'Hai, Admin {namaadmin}')
# daftar_admin= {'1345' : 'Nadia', '3212': 'Tonny' }
# admin= input ('Masukkan kode pegawai=  ')
# admin=daftar_admin.get(admin,'kode gaada')


# pembukaan(admin,'SIDO MAKMUR SELALU ADA')


# pendapatan=1500000
# saldo=2000000
# def pembukaan(namaPT,namaAdmin):

#     print('==========================')
#     print(f'selamat datang di PT namaPt')
#     print('==========================')
#     print(f'Hai admin {namaAdmin}')
#     pilih=input(f'pendapatan kemarin adalah Rp{pendapatan} , apakah anda ingin menambahkan pendapatan ke saldo?\n(y/n)\n')
#     if pilih == 'y':
#         print(f'saldo sekarang adalah Rp. {tambah_saldo(pendapatan)}')
#     else:
#         print('peringatan : pendapatan kemarin belum direkap')

# def tambah_saldo(dt):
#     global saldo
#     saldo += dt
#     return saldo
# daftar_admin = {'1345':'Nadia','3212':'Tonny'} 
# admin=input('masukan kode pegawai= ')
# pembukaan('sido makmur selalu', daftar_admin[admin])



def tambah_siswa(daftar_siswa):
    nama = input ('Masukkan nama siswa: ')
    kelas=input('Masukkan kelas siswa: ')
    try:
        nilai=float(input('Masukkan nilai siswa: '))
    except ValueError:
        print('Nilai tidak valid. Harap masukan angka.')
        return daftar_siswa 

    siswa_baru={'nama': nama, 'kelas': kelas, 'nilai': nilai}
    daftar_siswa.append(siswa_baru)
    print(f'Siswa {nama} berhasil ditambahkan.')
    return daftar_siswa

def tampilkan_siswa(daftar_siswa):
    if not daftar_siswa:
        print('belum ada data siswa.')
        return
    
    print('data siswa: ')
    print('-' * 30)
    print('{:<15} | {:<10} | {:<5}'.format('Nama', 'Kelas', 'Nilai'))
    print('-' * 30)
    for siswa in daftar_siswa:
        print('{:<15} | {:<10} | {:<5.2f}'.format(siswa['nama'], siswa['kelas'], siswa['nilai']))
    print('-' * 30)

def hapus_siswa(daftar_siswa, nama_dihapus):
    for i in range(len(daftar_siswa)):
        if daftar_siswa[i]['nama'].lower()== nama_dihapus.lower():
            del daftar_siswa[i]
            print(f'Siswa dengan nama {nama_dihapus} berhasil dihapus.')
            return daftar_siswa
    print(f'Siswa dengan nama {nama_dihapus} tidak ditemukan.')

daftar_siswa = []

while True:
    print('\nMenu manajemen data siswa: \n1. Tambah Siswa \n2. Tampilkan semua Siswa \n3. Hapus Siswa \n0. Keluar')

    pilihan = input('Pilih menu (1/2/3/0): ')

    if pilihan == '1':
        daftar_siswa = tambah_siswa(daftar_siswa)
    elif pilihan == '2':
        tampilkan_siswa(daftar_siswa)
    elif pilihan == '3':
        nama_dihapus = input('Masukkan nama siswa yang ingin dihapus: ')
        hapus_siswa(daftar_siswa, nama_dihapus)
    elif pilihan == '0':
        break
    else:
        print('Pilihan tidak valid. Silakan coba lagi.')