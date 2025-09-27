pituus = float(input("Anna kuhan pituus (cm): "))

if pituus < 37:
    puuttuu = 37 - pituus
    print(f"Kuha on alamittainen. Laske se takaisin järveen.")
    print(f"Se on {puuttuu:.1f} cm liian lyhyt.")
else:
    print("Kuha on sallitun mittainen, voit pitää sen.")
