luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Syöte ei ollut kelvollinen luku.")

if luvut:
    print("Pienin luku:", min(luvut))
    print("Suurin luku:", max(luvut))
else:
    print("Et antanut yhtään lukua.")

