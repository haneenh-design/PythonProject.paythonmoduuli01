sukupuoli = input("Anna sukupuoli (mies/nainen): ").lower()
arvo = int(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if arvo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif arvo > 175:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")
elif sukupuoli == "mies":
    if arvo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif arvo > 195:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")
else:
    print("Virheellinen sukupuoli.")
