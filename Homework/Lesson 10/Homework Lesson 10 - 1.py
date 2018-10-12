# Homework Lesson 10 - 1

trajectBruin = {
  "Boxtel", "Best", "Beukenlaan", "Eindhoven", "Helmond 't Hout", "Helmond", "Helmond Brouwhuis", "Deurne"
}

trajectGroen = {
  "Boxtel", "Best", "Beukenlaan", "Eindhoven", "Geldrop", "Heeze", "Weert"
}

overeenkomst = trajectBruin.intersection(trajectGroen)
print(overeenkomst)

verschilBruin = trajectBruin.difference(trajectGroen)
print(verschilBruin)

totaleLijst = set()
for item in trajectBruin.intersection(trajectGroen):
  totaleLijst.add(item)

for item in trajectBruin.difference(trajectGroen):
  totaleLijst.add(item)

for item in trajectGroen.difference(trajectBruin):
  totaleLijst.add(item)

print(totaleLijst)
