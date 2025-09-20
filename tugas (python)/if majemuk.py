# # # # def jumlahkan(a, b):
# # # #     hasil = a + b
# # # #     return hasil
# # # # hasil = jumlahkan(5, 3)
# # # # print(f" hasilnya yaitu {hasil}") 

# # # # def jumlah(a, b):
# # # #     hasil= a* b
# # # #     return hasil
# # # # hasil=jumlah(900,8000)
# # # # print(f"hasil dari perkaliannya yaitu:{hasil} ,terimakasih :)")

# # # x=3
# # # y=6
# # # if x>y:
# # #     x=x+3
# # #     y=y-2
# # # elif x==y:
# # #     x*5
# # #     y=y/2
# # # else:
# # #     x=x+10
# # #     y=y*2
# # # print(x)
# # # print(y)

# # nilai=int(input("Hasil ujian siswa: "))
# # if nilai >=90:
# #     print("A")
# # elif nilai >=80:
# #     print("B")
# # elif nilai <70:
# #     print("C")
# # else:
# #     print("GA NAIK TOLOL, BELAJAR LAGI SANA!")

# age=int(input("""Nightclub (only for 18+ only)
# What is yo age lil boy?
# :"""))

# if age <17:
#     print("GET OUT!!")
# elif age >= 18:
#     print("wanna drink with me honey?? :3")

# if majemuk

# a=90
# b=900

# if a>b:
#     print("ok")
# elif a==b:
#     print("ok, tapi rasa alpukat")
# else:
#     print("okoklah")
import time

def type_effect(text, delay=0.9):
    for char in text:
        print(char, end='', flush=True) 
        time.sleep(delay)
    

welcome=str(input("""what r u up to?
                  
[bar]
[shop]
""")).lower()
if welcome==("bar"):
    ages=int(input("""what is your ages lil boy?
"""))
    if ages > 17:
        inside_bar=str(input("""
hey boy, what r u doing here?
[drink]
[partying w/girls]
[nothing]
"""))
        if inside_bar==("drink"):
                print("okay, enjoy your drink")
        elif inside_bar==("partying w/girls"):
                print("dance with me till im die my honey XD")
        elif inside_bar==("nothing"):
                print("really? nothing? you wasted my time fr >:(")
    else:
        card=str(input("""you're too young for this, you dont even have a pass card LOL
[i have]      [dont have]
"""))
        if card == ("i have"):
            pass_card=("damn, you can come in kid")
            inside_bar=str(input("""
hey boy, what r u doing here?
[drink]
[partying w/girls]
[nothing]
"""))
            if inside_bar==("drink"):
                print("okay, enjoy your drink")
            elif inside_bar==("partying w/girls"):
                print("dance with me till im die my honey XD")
            elif inside_bar==("nothing"):
                print("really? nothing? you wasted my time fr >:(")

        elif card==("dont have"):
            print("then you must get out now! >:(")

if welcome == ("shop"):
    item=str(input("""what r u gonna buy?
1. potion (500g)
2. mana potion (550g)
3. sword (10.000g)
4. shield (9.000g)
"""))
    if item==("potion"):
        potion=int(input("""how much you want? (max is 500)
"""))
        if potion<501:
            print("ok, heres your potion :D")
        else:
            print("""i said max is 500, why u dont read that? >:(, i not on my mood rn
closing shop""")
    if item==("mana potion"):
        mana=int(input("""how much you want? (max is 500)
"""))
        if mana<5001:
            print("ok, heres your potion :D")
        else:
            print("""i said max is 500, why u dont read that? >:(, i not on my mood rn
closing shop""")
    if item==("sword"):
        print("ok, heres your sword, have a nice day :D")
    if item==("shield"):
        print("ok, heres your shield, have anice day :D")
print() 