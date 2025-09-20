# # import time

# # kalimat="contoh dely antar kata"
# # kata_kata= kalimat.split()

# # for kata in kata_kata:
# #     print(kata, end=" ", flush=True)
# #     time.sleep(1)

# import time 
# kalimat="contoh kalimat delay"
# for huruf in kalimat:
#     print(huruf, end="", flush=True)
#     time.sleep(0.1)
kalimat="poke poke apa yng mewing? pukimak"

def delay():
    for _ in range(100):
        pass

for huruf in kalimat:
    print(huruf, end="", flush=True)
    delay()