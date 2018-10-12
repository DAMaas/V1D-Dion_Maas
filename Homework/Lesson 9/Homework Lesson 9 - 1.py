# Homework Lesson 9 - 1

gebruikerGetallenLijst = []

while True:
  gebruikerInvoer = int(input("Geef een getal: "))
  if gebruikerInvoer != 0:
    gebruikerGetallenLijst.append(gebruikerInvoer)
  else:
    aantalGetallenIngevoerd = len(gebruikerGetallenLijst)
    somVanGetallen = sum(gebruikerGetallenLijst[0:])
    print("Er zijn " + str(aantalGetallenIngevoerd) + " getallen ingevoerd, de som is: " + str(somVanGetallen))
    break
