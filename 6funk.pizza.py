import math

def yksikkohinta(halk_cm, hinta):
    """Laske pizzan yksikköhinnan €/m^2."""
    sade = halk_cm / 2
    pinta_ala = 3.14 * sade ** 2 / 10000
    return hinta / pinta_ala

# Pääohjelma
halk1 = float(input("Anna 1. pizzan halkaisija (cm)"))
hinta1 = float(input("Anna 1. pizzan hinta:"))

halk2= float(input("Anna 2. pizzan halkaisija (cm)"))
hinta2 = float(input("Anna 2. pizzan hinta:"))

yks1 = yksikkohinta(halk1, hinta1)
yks2 = yksikkohinta(halk2, hinta2)

print(f"1. pizzan yksikköhinta: {yks1:.2f} €/m²")
print(f"2. pizzan yksikköhinta: {yks2:.2f} €/m²")

if yks1 < yks2:
    print("1. pizza on parempi ostos.")
elif yks2 < yks1:
    print("2. pizza on parempi ostos.")
else:
    print("Pizzat ovat yhtä hyviä.")
