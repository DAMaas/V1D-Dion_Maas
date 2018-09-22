# Homework Lesson 5 - 3

leeftijd = input("Geef je leeftijd: ")
heeftPaspoort = input("Nederlands paspoort (ja of nee): ")

if int(leeftijd) >= 18 and heeftPaspoort == "ja":
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Je mag niet stemmen")