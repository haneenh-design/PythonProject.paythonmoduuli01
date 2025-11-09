lentoasemat = {}

while True:

    print("﹨nValitse toiminto:")
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoaseman tiedot")
    print("3 = Lopeta")

    valinta = input("Valinta: ")

    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input ("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f" Lentoasema {nimi} (koodi {icao} tallennettu!")

    elif valinta == "2":
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"{icao}: {lentoasemat[icao]}")

        else:
            print("Tuntematon ICAO-koodi.")
    elif valinta == "3":
        print("Ohjelma lopetetaan. Kiitos!")
        break

    else:
        print("Virhellinen valinta, yritä uudelleen.")
