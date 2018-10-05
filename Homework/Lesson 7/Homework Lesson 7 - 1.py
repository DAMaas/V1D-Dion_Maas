# Homework Lesson 7 - 1


def convert(tempCelsius):
    res = ((tempCelsius*1.8)+32)
    return res


def table(vanafTemp, totTemp, gradenPerStap):
    print('{:5}   {:5}'.format("  F  ", "  C  "))
    for tempCelsius in range(vanafTemp, totTemp, gradenPerStap):
        tempFahrenheit = convert(tempCelsius)
        print('{:5}   {:5}'.format(tempFahrenheit, float(tempCelsius)))

print(table(-30, 50, 10))
