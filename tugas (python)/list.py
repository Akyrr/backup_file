#create list

angka=[10,20,30,40,50,60,70,80,90,100]
string=['apel', 'kayu', 'bangku', 'hanya cinta dan malam']
desimal=[0.90,90.800,5.0,2.0]

rand=[17,'perempuan','Malang']
# print(rand)

#Read list
namaBuah=['jeruk','mangga','semangka','mangga']
#print(namaBuah) #[0],[0:2]


#Insert list
fruit=['jeruk','mangga','semangka','mangga']
# print(fruit)
fruit.append('anggur')
fruit.insert(2,'leci')
# print(fruit)

fruity=['jeruk','mangga','semangka','mangga']
veggie=['wortel','tomat']
# print(f'ni buah {fruity}')
# print(f'ni sayur {veggie}')
fruity.extend(veggie)
# print(f'ni buah setelah perubahan {fruity}')
# print(f'ni sayur setelah perubahan {veggie}')


#Update list
fruita=['jeruk','mangga','semangka','mangga']
# print(f'daftar buah before {fruita}')
fruita[1:3]=['kelengkeng','anggur']
print(f'daftar buah setelah before {fruita}')


#Delete list
fruiti=['jeruk','mangga','semangka','mangga']
fruiti.pop(1)
# print(fruiti)
# print(k)

fruiti1=['jeruk','mangga','semangka','mangga']
fruiti1.remove('mangga')
# print(fruiti1)

fruiti2=['jeruk','mangga','semangka','mangga']
del fruiti2[0]
# print(fruiti2)

fruiti3=['jeruk','mangga','semangka','mangga']
# fruiti3.clear()
# print(fruiti3)