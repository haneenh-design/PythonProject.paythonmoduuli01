def gallonat_litroiksi(gallonat) :
    """palauttaa gallonat litroina (1 gallona = 3.875 litraa)."""
    return gallonat * 3.785

    # pääohjelma
    while True:
        gallonat = float(input("Anna gallonamäärä (negatiivinen lopettaa): "))
        if gallonat < 0:
            print ("Ohjelma päättyy.")
            break
        litrat = gallonat_litroiksi(gallonat)
        print(f"Vastaus: {litrat:.2f} litraa")
