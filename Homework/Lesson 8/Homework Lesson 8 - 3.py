# Homework Lesson 8 - 3

invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoerGesplitst = invoer.split("-")
invoerGesplitst.sort()
invoerMin = min(invoerGesplitst)
invoerMax = max(invoerGesplitst)
invoerAantal = len(invoerGesplitst)
invoerSom = sum(int(i) for i in invoerGesplitst[0:])
invoerGemiddelde = invoerSom / invoerAantal

print("Gesorteerde list van ints: " + str(invoerGesplitst))
print("Grootste getal: " + str(invoerMax))
print("Kleinste getal: " + str(invoerMin))
print("Aantal getallen: " + str(invoerAantal))
print("Som van de getallen: " + str(invoerSom))
print("Gemiddelde van de getallen: " + str(invoerGemiddelde))
