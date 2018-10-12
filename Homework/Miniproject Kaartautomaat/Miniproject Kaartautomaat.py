# Miniproject Kaartautomaat

def inlezen_beginstation(stations):
    while True:
        inputBeginstationnaam = input("Vanaf welk station vertrek je? ")
        if inputBeginstationnaam not in stations:
            print("Dat is geen geldig beginstation!")
        else:
            return inputBeginstationnaam

def inlezen_eindstation(stations, beginstation):
    while True:
        inputEindstationnaam = input("Naar welk station reis je? ")
        if inputEindstationnaam not in stations:
            print("Dat is geen geldig eindstation!")
        else:
            return inputEindstationnaam

def omroepen_reis(stations, beginstation, eindstation):
    beginstationNummer = stations.index(beginstation)
    eindstationNummer = stations.index(eindstation)
    tussenliggendeStations = (stations.index(eindstation) - stations.index(beginstation)) - 1
    print("Het beginstation, " + beginstation + ", is het " + str(beginstationNummer + 1) + "e station in het traject")
    print("Het eindstation, " + eindstation + ", is het " + str(eindstationNummer + 1) + "e station in het traject")
    print("Tussen " + beginstation + " en " + eindstation + " zit(ten) " + str(tussenliggendeStations) + " halte(s)")
    print("De prijs van jouw reis bedraagt €" + str(tussenliggendeStations * 5))
    print()
    print("Zo ziet jouw route er uit:")
    print("O> " + beginstation)
    for item in stations[(beginstationNummer + 1):(eindstationNummer - 1)]:
        print("-> " + item)
    print("O> " + eindstation)

stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)