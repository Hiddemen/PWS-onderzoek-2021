# input van de gebruiker
review = input("Schrijf hier uw review: ")


# input wordt in kleine letters gezet
review = review.lower()


# lijst met positieve en negatieve woorden
positieveWoorden = ["leuk", "goed", "perfect", "efficiënt", "top", "fijn", "plezierig", "prima"]
puntenAantalPositief = [1, 2, 3, 2, 3, 1, 2, 1]

negatieveWoorden = ["stom", "slecht", "belabberd", "matig", "teleurstellend", "jammer", "irritant", "spijtig"]
puntenAantalNegatief = [1, 2, 3, 1, 2, 1, 2, 1]


# tellers om het aan positieve en negatieve woorden te tellen
positieveWoordenPunten = 0
negatieveWoordenPunten = 0


# loop die opniew gaat voor elk woord in de positieveWoorden lijst
for x in positieveWoorden:

    # Als woord x uit de lijst in de review staat wordt er 1 bij de positieveWoordenCounter opgeteld
    if x in review:
        positieveWoordenPunten = positieveWoordenPunten + puntenAantalPositief[positieveWoorden.index(x)]



# loop die opniew gaat voor elk woord in de negatieveWoorden lijst
for x in negatieveWoorden:

    # Als woord x uit de lijst in de review staat wordt er 1 bij de negatieveWoordenCounter opgeteld
    if x in review:
        negatieveWoordenPunten = negatieveWoordenPunten + puntenAantalNegatief[negatieveWoorden.index(x)]



# print het aantal positieve ene negatieve woorden
print("Aantal positieve punten: ", positieveWoordenPunten)
print("Aantal negatieve punten: ", negatieveWoordenPunten)


# als er meer negatieve woorden dan positieve woorden in review zit wordt er geprint dat het negatief is.
# enzovoort voor positief en neutraal
if negatieveWoordenPunten > positieveWoordenPunten:
    print("De review is negatief")

elif positieveWoordenPunten > negatieveWoordenPunten:
    print("De review is positief")

elif positieveWoordenPunten == negatieveWoordenPunten:
    print("De review is neutraal")