import random

oikea_luku = random.randint(1, 10)

while True:
    try:
        arvaus = int(input("Arvaa luku (1–10): "))
        if arvaus < oikea_luku:
            print("Liian pieni arvaus.")
        elif arvaus > oikea_luku:
            print("Liian suuri arvaus.")
        else:
            print("Oikein!")
            break
    except ValueError:
        print("Syötä vain kokonaisluku.")
