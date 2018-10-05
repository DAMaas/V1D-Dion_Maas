# Homework Lesson 7 - 3


def readFileLength():
    filepath = input("What is the path to the file? ")
    fileInput = open(filepath)
    fileData = fileInput.readlines()
    fileInput.close()
    fileLines = len(fileData)
    output1 = "Deze file telt " + str(fileLines) + " regels"
    output2Index = fileData.index(max(fileData))
    output2Clean = fileData[output2Index].split(",")
    output2 = "Het grootste kaartnummer is: " + str(output2Clean[0]) + " en dat staat op regel " + str(output2Index + 1)
    return print(output1), print(output2)

readFileLength()