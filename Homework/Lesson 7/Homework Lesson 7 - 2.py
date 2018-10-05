# Homework Lesson 7 - 2


def readFile():
    filepath = input("What is the path to the file? ")
    fileInput = open(filepath)
    fileData = fileInput.readlines()
    fileInput.close()
    for everything in fileData:
        everythingNoNewline = everything.replace("\n", "")
        separatedLines = everythingNoNewline.split(", ")
        print('{} heeft kaartnummer: {}'.format(separatedLines[1], separatedLines[0]))
    return

readFile()