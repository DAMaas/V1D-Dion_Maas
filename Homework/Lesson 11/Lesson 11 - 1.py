# Homework Lesson 11 - 1


class NegativeNumberError(UserWarning):
    pass


while True:
    try:
        totaalBedrag = 4356
        strAantalPersonen = input("Hoe veel personen gaan er mee? ")
        intAantalPersonen = int(strAantalPersonen)
        if intAantalPersonen < 0:
            raise NegativeNumberError
        bedragPerPersoon = totaalBedrag / intAantalPersonen
        print("Het bedrag per persoon is " + str(bedragPerPersoon))
        break
    except NegativeNumberError:
        print("Negatieve getallen zijn niet toegestaan!")
    except ZeroDivisionError:
        print("Delen door nul kan niet!")
    except ValueError:
        print("Gebruik cijfers voor het invoeren van het aantal!")
    except:
        print("Onjuiste invoer!")