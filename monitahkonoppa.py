import random

def heitto_noppa(tahkot):
    """Palauttaa satunnaisen silmäluvun 1 - tahkojen määrä."""
    silmaluku = random.randint(1, tahkot)
    print("Heitto:", silmaluku)
    return silmaluku

# Pääohjelma
tahkot = int(input("Anna nopan tahkojen määrä: "))

while True:
    luku = heitto_noppa(tahkot)
    if luku == tahkot:
        print("saatiin suurin silmäluku Lopetetaan.")
        break