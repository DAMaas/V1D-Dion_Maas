# Miniproject NS

afstandKM = 0
leeftijd = 0
weekendrit = False
magLeeftijdKorting = leeftijd < 12 or leeftijd >= 65

def standaardprijs(afstandKM):
    prijs = 0
    prijsPerKM = 0.80
    vastBedragVanafVijftigKM = 15
    goedkoperePrijsVanafVijftigPerKM = 0.60

    if afstandKM > 0:
        if afstandKM <= 50:
            prijs = afstandKM * prijsPerKM
        elif afstandKM > 50:
            prijs = vastBedragVanafVijftigKM + (afstandKM * prijsPerKM)
    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    basisPrijs = standaardprijs(afstandKM)
    kortingPercentage = 0

    if magLeeftijdKorting:
        if weekendrit:
            kortingPercentage = 35
        else:
            kortingPercentage = 30
    elif weekendrit:
        kortingPercentage = 40

    kortingPrijs = basisPrijs - ((basisPrijs / 100)*kortingPercentage)
    return kortingPrijs

print(ritprijs(11, False, 100))
print(ritprijs(12, False, 200))
print(ritprijs(64, False, 300))
print(ritprijs(65, False, 400))

print(ritprijs(11, True, 100))
print(ritprijs(12, True, 200))
print(ritprijs(64, True, 300))
print(ritprijs(65, True, 400))

print(ritprijs(11, False, -100))
print(ritprijs(12, False, -200))
print(ritprijs(64, False, 3))
print(ritprijs(65, False, 4))

print(ritprijs(11, True, 1))
print(ritprijs(12, True, 2))
print(ritprijs(64, True, -300))
print(ritprijs(65, True, -400))
