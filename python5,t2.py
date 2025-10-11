from pienen_suurin import luvut
luvut = []
while True:
    syote = input (" Anna luku (Enter lopettaa): ")
    if syote == "":
        break
        luku = int(syote)
        luvut.append(luku)

luvut.sort(reverse=True)
print("Viisi suurinta lukua:")

for luku in luvut [:5:]
    print(luku)
