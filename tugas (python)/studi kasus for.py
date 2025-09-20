kataposfitif=['baik','bagus','keren','5','imut','rekomen','berkualitas','suka','sukak','lima','cepat','ramah']
katanegatif=['jelek','rusak','1','buruk','kecewa','lama','penyok','bau']

komentar=input('Terimkakasih sudah membeli AMBALABU dari toko NGAWI OFFICIAL.\nApakah kamu puas dengan produknya? bagaimana pendapatmu?\n\n')
komentar=komentar.lower()
katakomentar=komentar.split()
positif=0
negative=0

for a in katakomentar:
    if a in kataposfitif:
        positif+=1
    elif a in katanegatif:
        negative+=1

if positif>negative:
    print('Komentar baik terdeteksi!!!!!!')
elif negative>positif:
    print('Komentar buruk terdeteksi!!!!!')
else:
    print('Komentar netral terdeteksi!!!!')