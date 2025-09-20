# for x in range(2,5):
#     print(x) 

# for x in 'soto':
#     print(x)

# namabuah = ["apel","jeruk","semangka"]
# for buah in namabuah :
#     print (buah)

# nilai=1
# while nilai<5:
#     print('helo ke-',nilai)
#     nilai+=1 #yang hilang itu data dari variabel "nilai"

nilai = 0
while nilai < 7:
    nilai+=3
    print (f'Hello ke-{nilai}') #tidak ada increment, harusnya ada; nilai +=1


# jumlahkata=0 #penambahan variabel dengan nilai 0 agar bisa dihitung oleh jumlahkata+=1
# kalimat=input("masukan kalimatmu...:")
# kata=kalimat.split()
# for perkata,tiapkata in enumerate(kata): #penambahan enumerate() agar bisa meng-iterasi list
#     jumlahkata += 1
#     print (f"<{tiapkata}> adalah kata ke-{perkata+1}")

import random 
angka_rahasia=random.randint(1,100)
tebakan=0
percobaan=0
print("Hai, ayo bermain tebak angka!\nSaya telah memilih angka antara 1 sampai 100.")
while tebakan!=angka_rahasia:
    try:
        tebakan=int(input("Tebakan anda: "))
        percobaan+=1
        if tebakan<angka_rahasia:
            print('terlalu rendah. Coba lagi!')
        elif tebakan>angka_rahasia:
            print('terlalu tinggi. Coba lagi!')
    except ValueError:
        print('masukan angka yang valid!')
print(f'Selamat! anda berhasil menebak dalam {percobaan} percobaan')