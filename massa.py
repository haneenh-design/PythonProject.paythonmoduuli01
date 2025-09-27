# Keskiaikaiset mitat:
# 1 leiviskä = 20 naulaa
# 1 naula = 32 luotia
# 1 luoti = 13.3 grammaa

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Muutetaan kaikki grammoiksi
grammat = (leiviskat * 20 * 32 * 13.3) + (naulat * 32 * 13.3) + (luodit * 13.3)

# Erotellaan kilot ja loput grammat
kilot = int(grammat // 1000)   # kokonaiset kilot
grammat = grammat % 1000       # jäljelle jääneet grammat

print("Massa nykymittojen mukaan:")
print(f"{kilot} kilogrammaa ja {grammat:.2f} grammaa.")
