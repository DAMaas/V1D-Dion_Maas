# Homework Lesson 3

# 1 - 1

favorieten = ["Alison Wonderland"]
print(favorieten)
# Output = ['Alison Wonderland']

# 1 - 2

favorieten.append("Lido")
print(favorieten)
# Output = ['Alison Wonderland', 'Lido']

# 1 - 3

favorieten[1] = "Boris Brejcha"
print(favorieten)
# Output = ['Alison Wonderland', 'Boris Brejcha']



# 2 - 1

numberlist1 = [3, 7, -2, 12]
numberlist2 = [54, -32, 3, -88, 66]

print( abs( min(numberlist1) - max(numberlist1) ) )
# Output = 14
print( abs( min(numberlist2) - max(numberlist2) ) )
# Output = 154



# 3 - 1

letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')

lettersOccurrence = [letters.count("A"), letters.count("B"), letters.count("C")]
print(lettersOccurrence)