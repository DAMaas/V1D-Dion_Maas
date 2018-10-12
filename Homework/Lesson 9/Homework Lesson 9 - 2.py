# Homework Lesson 9 - 2

while True:
  gebruikerInvoer = input("Geef een string van 4 letters: ")
  if len(gebruikerInvoer) != 4:
    lengteGebruikerInvoer = len(gebruikerInvoer)
    print(gebruikerInvoer + " heeft " + str(lengteGebruikerInvoer) + " letters")
  else:
    print("Inlezen van correcte string: " + gebruikerInvoer + " is geslaagd")
    break
