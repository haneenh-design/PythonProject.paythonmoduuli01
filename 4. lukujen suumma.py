def laske_summa (lista) :
    """palauttaa listan lukujen summan."""
    return sum(lista)

# Pääohjelma
luvut = [5, 6, 7, 8]
summa = laske_summa(luvut)
print("Listan summa on:", summa)