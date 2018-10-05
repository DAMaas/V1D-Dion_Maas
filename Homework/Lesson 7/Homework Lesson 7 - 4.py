# Homework Lesson 7 - 4

import datetime

def hardlopers():
    while True:
        inputFile = 0
        naamHardloper = input("Wie ging er net over de finish? (De tijd wordt geregisteerd op het moment dat je op enter drukt) (Typ exit om te stoppen): ")
        if naamHardloper == "exit":
            break
        else:
            vandaag = datetime.datetime.today()
            geformatteerdeTijd = vandaag.strftime("%a %d %b %Y, %H:%M:%S, ")
            inputFile = open("Hardlopers.txt", "a")
            inputFile.write(geformatteerdeTijd + naamHardloper + "\n")
    return inputFile

hardlopers()