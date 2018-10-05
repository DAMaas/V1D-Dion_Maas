# Homework Lesson 7 - 5

def gemiddelde():
    while True:
        inputString = "str"
        willekeurigeString = input("Typ een willekeurige zin (Typ exit om te stoppen): ")
        if willekeurigeString == "exit":
            break
        else:
            totaleLengte = 0
            totaleWoorden = 0
            willekeurigeStringGescheiden = willekeurigeString.split(" ")
            for word in willekeurigeStringGescheiden:
                totaleLengte += len(word)
                totaleWoorden += 1
            print("De gemiddelde woordlengte is " + str(totaleLengte / totaleWoorden))
    return

gemiddelde()