# Homework Lesson 9 - 5

def namen():
  namenDictionary = {}
  while True:
    naamInput = input("Geef een naam op: ")
    if naamInput == "":
      print()
      break
    elif naamInput not in namenDictionary:
      namenDictionary[naamInput] = 1
    else:
      namenDictionary[naamInput] = namenDictionary[naamInput] + 1
  return namenDictionary

namenDictionary = namen()

for key in namenDictionary:
  if namenDictionary[key] > 1:
    print("Er zijn " + str(namenDictionary[key]) + " mensen met de naam " + key)
  else:
    print("Er is 1 iemand met de naam " + key)
