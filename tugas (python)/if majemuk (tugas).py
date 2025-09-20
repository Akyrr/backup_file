# jika waktu perjalanan kurang dari 30 menit dan jarak tempuh kurang dari 10km, tarif dasar adalah
# rp. 15.000. jika waktu perjalanan lebih dari 30 menit/jarak tempuh lebih dari 10km, tarif dasar
# adalah rp. 20.000. untuk setiap km tambahan setelah 10km pertama akan dikenakan biaya tambahan rp2.000


print("         [Go-Go!]")

waktu=int(input("\nWaktu perjalanan yang ditempuh(per menit)\n"))
jarak=int(input("\nJarak yg ditempuh (per km)\n"))

if waktu <= 30 and jarak <= 10:
    print(f"[Total]\nWaktu perjalanan:{waktu} menit\nJarak tempuh:{jarak} km\nTarif dari perjalanan kamu yaitu Rp.15.000\n\nTerimakasih sudah menggunakan Go-Go :)")
    
elif waktu >30 and jarak >10:
    tambahan=jarak-10
    biaya=tambahan*2000+20000
    print(f"[Total]\nWaktu perjalanan:{waktu} menit\nJarak tempuh:{jarak} km\nBiaya tambahan:{jarak} - 10 x Rp.2000 + Rp.20.000\n               = Rp.{biaya}\n\nTerimakasih sudah menggunakan Go-Go :)""")
    
elif waktu >30 and jarak <10:
    print(f"[Total]\nWaktu perjalanan:{waktu} menit\nJarak perjalanan:{jarak} km\n\nTarif dari perjalanan kamu yaitu Rp.20.000")
    
elif waktu <30 and jarak >10:
    jaraktambahan= jarak-10
    biayaextra= jaraktambahan*2000+20000
    print(f"[Total]\nWaktu perjalanan:{waktu} menit\nJarak perjalanan:{jarak} km\nBiaya tambahan:{jarak} - 10 x Rp.2000 + Rp.20.000\n               = Rp.{biayaextra}\n\nTerimakasih sudah menggunakan Go-Go :)""")