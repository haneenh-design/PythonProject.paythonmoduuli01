import math
import random

while True:
    print("\nValikko")
    print("1: Tervehdys")
    print("2: Ympyrän pinta-ala")
    print("3: Suorakulmio (piiri ja pinta-ala)")
    print("4: Kolme kokonaislukua (summa, tulo, keskiarvo)")
    print("5: Keskiaikainen massa -> kilogrammoiksi ja grammoiksi")
    print("6: Numerolukon koodit")
    print("0: Lopeta")

    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        nimi = input("Anna nimesi: ")
        print(f"Terve, {nimi}!")

    elif valinta == "2":
        sade = float(input("Anna ympyrän säde: "))
        pinta_ala = math.pi * (sade ** 2)
        print(f"Ympyrän pinta-ala on {pinta_ala:.2f}")

    elif valinta == "3":
        kanta = float(input("Anna suorakulmion kanta: "))
        korkeus = float(input("Anna suorakulmion korkeus: "))
        piiri = 2 * (kanta + korkeus)
        pinta_ala = kanta * korkeus
        print(f"Suorakulmion piiri on {piiri}")
        print(f"Suorakulmion pinta-ala on {pinta_ala}")

    elif valinta == "4":
        luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
        luku2 = int(input("Anna toinen kokonaisluku: "))
        luku3 = int(input("Anna kolmas kokonaisluku: "))
        summa = luku1 + luku2 + luku3
        tulo = luku1 * luku2 * luku3
        keskiarvo = summa / 3
        print(f"Lukujen summa: {summa}")
        print(f"Lukujen tulo: {tulo}")
        print(f"Lukujen keskiarvo: {keskiarvo:.2f}")

    elif valinta == "5":
        leiviskat = float(input("Anna leiviskät: "))
        naulat = float(input("Anna naulat: "))
        luodit = float(input("Anna luodit: "))
        grammat = (leiviskat * 20 * 32 * 13.3) + (naulat * 32 * 13.3) + (luodit * 13.3)
        kilot = int(grammat // 1000)
        grammat = grammat % 1000
        print(f"Massa nykymittojen mukaan:")
        print(f"{kilot} kilogrammaa ja {grammat:.2f} grammaa.")

    elif valinta == "6":
        koodi1 = "".join(str(random.randint(0, 9)) for _ in range(3))
        koodi2 = "".join(str(random.randint(1, 6)) for _ in range(4))
        print(f"Kolminumeroinen koodi: {koodi1}")
        print(f"Nelinumeroinen koodi: {koodi2}")

    elif valinta == "0":
        print("Ohjelma loppuu. Hei hei!")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")
