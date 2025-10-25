import random

def heitto_noppa():
   """palauttaa satunnaisen silmäluvun 1-6."""
   silmaluku = random.randint(1,6)
   print("Heitto:", silmaluku)
   return silmaluku

# Pääohjelma
while True:
    luku = heitto_noppa()
    if luku == 6:
        print("Saatiin kuutonen! Lopetetaan.")
        break

