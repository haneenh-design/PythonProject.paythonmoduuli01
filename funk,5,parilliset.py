def etsi_parilliset (lista) :
    """ palauttaa listasta vain parilliset luvut."""
    return [luku for luku in lista if luku % 2 == 0]

# Pääohjelma
luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
print("Alkuperäinen lista:", luvut)
parilliset = etsi_parilliset(luvut)
print("parilliset luvut:", parilliset)