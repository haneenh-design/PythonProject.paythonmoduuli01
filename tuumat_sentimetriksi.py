while True:
    tuumat = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))
    if tuumat < 0:
        print("Ohjelma lopetettu.")
        break
    cm = tuumat * 2.54
    print(f"{tuumat} tuumaa = {cm:.2f} cm")

