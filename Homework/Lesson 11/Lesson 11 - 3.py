# Homework Lesson 11 - 3

import csv

bestand = 'Gamers.csv'

with open(bestand, "r", newline="") as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=";")
    scores = []
    file = []
    for row in reader:
        scores.append(row[2])
        file.append(row)

    besteSpeler = file[scores.index(max(scores))]
    print("De hoogste score is: " + besteSpeler[2] + " op " + besteSpeler[1] + " behaald door " + besteSpeler[0])