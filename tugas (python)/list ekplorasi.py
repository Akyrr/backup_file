nilai=[78,80,90,85,80]
totalNilai=0
counter=1
for n in nilai :
    counter =+ 1
    print(f'nilai ke {counter} = {n}')
    totalNilai += n
rerataNilai = totalNilai / len(nilai) #kegunaan len() yaitu untuk menghitung berapa banyak elemen yang terdapat dalam suatu list, dictionary, set, ataupun tupple
print(f'Hasil rata rata nilai seluruh siswa adalah {rerataNilai}')