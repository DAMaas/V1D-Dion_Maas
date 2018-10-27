# Homework Lesson 11 - 2

import datetime
import csv

bestand = 'Inloggers.csv'

with open(bestand, "w", newline="") as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=";")
    writer.writerow(("datum", "naam", "voorl", "gbdatum", "email"))

    while True:
        naam = input("Wat is je achternaam? ")
        if naam == "einde":
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        datum = datetime.datetime.now()
        writer.writerow((datum, naam, voorl, gbdatum, email))