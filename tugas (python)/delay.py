# import time

# def delay(text, delay=0.05):
#     for char in text:
#         print(char, end='', flush=True)
#         time.sleep(delay)

# text="""Selamat Datang di Inomart!
# kamu mau beli apa?"""
# delay(text, 0.09)

# import time
# def msg(string):

#     for i in (string):
#         print(i,end='')
#         time.sleep(0.7)

# msg("woe pokeee")
# msg("halooo")
import time

# Fungsi untuk memberikan efek pengetikan lambat
def type_effect(text, delay=0.09):
    for char in text:
        print(char, end='', flush=True)  # flush=True memastikan output segera muncul
        time.sleep(delay)  # Jeda waktu untuk tiap karakter
    print()  # Menambahkan baris baru setelah selesai

# Program utama
welcome = str(input("""What are you up to?\n\n[bar]\n[shop]\n""")).lower()

if welcome == "bar":
    ages = int(input("What is your age, lil boy?\n"))
    if ages > 17:
        inside_bar = str(input("""
hey boy, what r u doing here?
[drink]
[partying w/girls]
[nothing]
"""))
        if inside_bar == "drink":
            type_effect("okay, enjoy your drink")  # Panggil type_effect dengan teks yang ingin dicetak
        elif inside_bar == "partying w/girls":
            type_effect("dance with me till I die, my honey XD")
        elif inside_bar == "nothing":
            type_effect("really? nothing? you wasted my time for real >:(")
    else:
        card = str(input("you're too young for this, you don't even have a pass card LOL\n[i have] [don't have]\n"))
        if card == "i have":
            type_effect("damn, you can come in, kid")
            inside_bar = str(input("""
hey boy, what r u doing here?
[drink]
[partying w/girls]
[nothing]
"""))
            if inside_bar == "drink":
                type_effect("okay, enjoy your drink")
            elif inside_bar == "partying w/girls":
                type_effect("dance with me till I die, my honey XD")
            elif inside_bar == "nothing":
                type_effect("really? nothing? you wasted my time for real >:(")
        elif card == "don't have":
            type_effect("then you must get out now! >:(")

if welcome == "shop":
    item = str(input("""what r u gonna buy?\n1. potion (500g)\n2. mana potion (550g)\n3. sword (10.000g)\n4. shield (9.000g)\n"""))
    if item == "potion":
        potion = int(input("how much do you want? (max is 500)\n"))
        if potion <= 500:
            type_effect("ok, here's your potion :D")
        else:
            type_effect("I said max is 500, why didn't you read that? >:( I'm not in the mood right now, closing shop")
    elif item == "mana potion":
        mana = int(input("how much do you want? (max is 500)\n"))
        if mana <= 500:
            type_effect("ok, here's your mana potion :D")
        else:
            type_effect("I said max is 500, why didn't you read that? >:( I'm not in the mood right now, closing shop")
    elif item == "sword":
        type_effect("ok, here's your sword, have a nice day :D")
    elif item == "shield":
        type_effect("ok, here's your shield, have a nice day :D")
