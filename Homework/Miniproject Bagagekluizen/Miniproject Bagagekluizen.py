from random import randrange


fileName = "Kluizen.txt"


def menuKeuze():
    print(
        "1: Ik wil een nieuwe kluis\n2: Ik wil mijn kluis openen\n3: Ik geef mijn kluis terug\n4: Ik wil weten hoeveel kluizen nog vrij zijn\n5: Ik wil stoppen")
    menuKeuzeMaken(int(input("Selecteer uw keuze: ")))


def menuKeuzeMaken(menuNummer):
    if menuNummer == 1:
        krijgLocker()
    elif menuNummer == 2:
        openLocker()
    elif menuNummer == 3:
        vrijeLocker()
    elif menuNummer == 4:
        print("Er zijn nog {} locker(s) over.".format(12 - len(krijgLockerVanBestand())))
    elif menuNummer == 5:
        exit()
    else:
        print("Dit is een niet geldig commando, probeer opnieuw.")


def willekeurigeCode():
    return str(randrange(0, 9999)).zfill(4)


def krijgLocker():
    lockerNummer = legeLockerNummer()
    code = willekeurigeCode()
    lockers = krijgLockerVanBestand()
    if (lockerNummer is not -1):
        lockers.append(str(lockerNummer) + "-" + str(code) + "\n")
        slaLockersOp(lockers)
        print("U heeft kluis {} met code {} gekregen".format(lockerNummer, code))
    else:
        input("Er zijn geen kluisjes meer beschikbaar, probeer later opnieuw.\nDruk op een toets om verder te gaan.")


def openLocker():
    lockerNummer = input("Geef uw kluisnummer op: ")
    code = input("Geef uw kluiscode op: ")
    if int(lockerNummer) > 0 and int(lockerNummer) < 13 and len(code) == 4 and openLockerMetCode(lockerNummer, code):
        print("Kluis {} wordt geopend.".format(lockerNummer))
    else:
        print("Foutieve code voor locker {}, probeer opnieuw.".format(lockerNummer))


def vrijeLocker():
    lockerNummer = input("Geef uw kluisnummer op: ")
    code = input("Geef uw kluiscode op: ")

    if int(lockerNummer) > 0 and int(lockerNummer) < 13 and len(code) == 4 and vrijeLockerMetCode(lockerNummer, code):
        print(
            "Kluis {} wordt vrijgegeven voor andere gebruikers.\n!Let op of al uw eigendommen uit uw kluis zijn!".format(
                lockerNummer))
    else:
        print("Foutieve code voor locker {}, probeer opnieuw.".format(lockerNummer))


def legeLockerNummer():
    lockers = krijgLockerVanBestand()
    used = False
    if len(lockers) < 12:
        for indexer in range(1, 13):
            used = False
            for locker in lockers:
                lockerNummer = str(locker).split("-")
                if str(lockerNummer[0]) == str(indexer):
                    used = True
            if not used:
                return indexer
    else:
        return -1


def krijgLockerVanBestand():
    with open(fileName, 'r') as file:
        lockers = file.readlines()
    return lockers


def slaLockersOp(lockerLijst):
    with open(fileName, 'w')as writer:
        for locker in lockerLijst:
            writer.write(str(locker))
    return True


def openLockerMetCode(lockerNummer, code):
    lockers = krijgLockerVanBestand()
    for locker in lockers:
        data = str(locker).split("-")
        if data[0] == lockerNummer:
            if str(data[1].strip()) == str(code):
                return True
    return False


def vrijeLockerMetCode(lockerNummer, code):
    lockers = krijgLockerVanBestand()
    for locker in lockers:
        data = str(locker).split("-")
        if data[0] == lockerNummer:
            if str(data[1].strip()) == str(code):
                lockers.remove(locker)
                slaLockersOp(lockers)
                return True
    return False


while True:
    menuKeuze()
