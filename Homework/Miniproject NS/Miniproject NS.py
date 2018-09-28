# Miniproject NS

afstandKM = 123
leeftijd = 69
weekendrit = True

def standaardprijs(afstandKM):
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

    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == True:
            kortingPercentage = 35
        else:
            kortingPercentage = 30
    elif weekendrit == True:
        kortingPercentage = 40

    kortingPrijs = basisPrijs - ((basisPrijs / 100)*kortingPercentage)
    return kortingPrijs

print(standaardprijs(afstandKM))
print(ritprijs(leeftijd, weekendrit, afstandKM))
