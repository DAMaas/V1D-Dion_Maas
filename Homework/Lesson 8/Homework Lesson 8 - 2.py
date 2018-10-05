# Homework Lesson 8 - 2

lijstGesorteerd = []

lijst = eval(input("Geef een lijst met minimaal 10 strings: "))

for word in lijst:
    if len(word) == 4:
        lijstGesorteerd.append(word)

print("De nieuw-gemaakte lijst met alle vier-letterige strings is:")
print(lijstGesorteerd)