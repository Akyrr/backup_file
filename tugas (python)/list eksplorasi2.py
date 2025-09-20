# hargaProduk=[32000,13000,15000,11000]
# namaProduk=['sunco', 'so klin','sun light','mie telor']
# totalBelanja=0
# counter=0
# index=0
# print('SELAMAT DATANG DI TOKO MAKMUR JAYA')
# print('DAFTAR PRODUK HARI INI')
# for np in namaProduk:
#     counter +=1
#     print(f'{counter}. {np} - Rp. {hargaProduk[counter-1]}')
#     index += 1
# print('5. Sudah/Tidak jadi')
# while True:
#     pilihan = int(input('Mau belanja apa hari ini (1/2/3/4/5) ?\n'))
#     if pilihan == 1:
#         totalBelanja += hargaProduk[0]
#     elif pilihan == 2:
#         totalBelanja += hargaProduk[1]
#     elif pilihan == 3:
#         totalBelanja += hargaProduk[2]
#     elif pilihan == 4:
#         totalBelanja += hargaProduk[3]
#     elif pilihan == 5:
#         break
#     else:
#         print('Mohon maaf pilihan tidak tersedia')
# print('==========================================================')
# print(f'Total belanja anda adalah Rp. {totalBelanja}\n')
# print('TERIMAKASIH SUDAH BERBELANJA')

# hargaProduk = [32000, 13000, 15000, 11000]
# nameProduk = ["Sunco", "So Klin", "Sun Light", "Mie Telor"]
# keranjang = []
# totalBelanja = 0

# print("SELAMAT DATANG DI TOKO MAKMUR JAYA")
# print("DAFTAR PRODUK HARI INI :")
# for i, (np, hp) in enumerate(zip(nameProduk, hargaProduk), start=1):
#     print(f"{i}. {np} - Rp. {hp}")
# print("5. Gak jadi belanja deh")
# print("6. Hapus item dari keranjang")

# while True:
#     pilihan = int(input("Mau belanja apa hari ini (1/2/3/4/5/6)? "))
#     if pilihan == 1:
#         keranjang.append(("Sunco", hargaProduk[0]))
#     elif pilihan == 2:
#         keranjang.append(("So Klin", hargaProduk[1]))
#     elif pilihan == 3:
#         keranjang.append(("Sun Light", hargaProduk[2]))
#     elif pilihan == 4:
#         keranjang.append(("Mie Telor", hargaProduk[3]))
#     elif pilihan == 5:
#         break
#     elif pilihan == 6:
#         if not keranjang:
#             print("Keranjang belanja kosong.")
#         else:
#             print("Daftar belanja Anda:")
#             for idx, item in enumerate(keranjang, start=1):
#                 print(f"{idx}. {item[0]} - Rp. {item[1]}")
#             hapus = int(input("Pilih nomor item yang ingin dihapus: "))
#             if 1 <= hapus <= len(keranjang):
#                 removed_item = keranjang.pop(hapus - 1)
#                 print(f"{removed_item[0]} telah dihapus dari keranjang.")
#             else:
#                 print("Nomor item tidak valid.")
#     else:
#         print("Mohon maaf, pilihan tidak tersedia.")

# print("=======================================================")
# print("DETAIL BELANJA")
# for idx, item in enumerate(keranjang, start=1):
#     print(f"{idx}. {item[0]} = Rp. {item[1]}")
#     totalBelanja += item[1]

# print("-------------------------------------------------------")
# print(f"Total Belanja anda adalah Rp. {totalBelanja}\n")
# print("TERIMA KASIH SUDAH BERBELANJA")

hargaProduk = [32000, 13000, 15000, 11000]
nameProduk = ["Sunco", "So Klin", "Sun Light", "Mie Telor"]
keranjang = []
totalBelanja = 0

print("SELAMAT DATANG DI TOKO MAKMUR JAYA")
print("DAFTAR PRODUK HARI INI :")
for i, (np, hp) in enumerate(zip(nameProduk, hargaProduk), start=1):
    print(f"{i}. {np} - Rp. {hp}")
print("5. Gak jadi belanja deh")
print("6. Hapus item dari keranjang")
print("7. Bayar")

while True:
    pilihan = input("Mau belanja apa hari ini (1/2/3/4/5/6/7)? ")
    if pilihan == "1":
        keranjang.append(("Sunco", hargaProduk[0]))
    elif pilihan == "2":
        keranjang.append(("So Klin", hargaProduk[1]))
    elif pilihan == "3":
        keranjang.append(("Sun Light", hargaProduk[2]))
    elif pilihan == "4":
        keranjang.append(("Mie Telor", hargaProduk[3]))
    elif pilihan == "5":
        print("Terima kasih, sampai jumpa!")
        break
    elif pilihan == "6":
        if not keranjang:
            print("Keranjang belanja kosong.")
        else:
            print("Daftar belanja Anda:")
            for idx, item in enumerate(keranjang, start=1):
                print(f"{idx}. {item[0]} - Rp. {item[1]}")
            hapus = int(input("Pilih nomor item yang ingin dihapus: "))
            if 1 <= hapus <= len(keranjang):
                removed_item = keranjang.pop(hapus - 1)
                print(f"{removed_item[0]} telah dihapus dari keranjang.")
            else:
                print("Nomor item tidak valid.")
    elif pilihan == "7":
        if not keranjang:
            print("Keranjang belanja kosong. Tidak ada yang perlu dibayar.")
        else:
            print("DETAIL BELANJA")
            for idx, item in enumerate(keranjang, start=1):
                print(f"{idx}. {item[0]} = Rp. {item[1]}")
                totalBelanja += item[1]
            print("-------------------------------------------------------")
            print(f"Total Belanja anda adalah Rp. {totalBelanja}")
            print("TERIMA KASIH SUDAH BERBELANJA")
            break
    else:
        print("Mohon maaf, pilihan tidak tersedia.")
