kerrat = int(input("kuinka monta kertaa heitetään arpokuutioita ?"))
import random

summa = 0
for i in range(kerrat):
    silmaluku = random.randint(1, 6)
    print(f"Heitto {i + 1}: {silmaluku}")
    summa += silmaluku

    print(f"Silmälukujen summa on: {summa}")
