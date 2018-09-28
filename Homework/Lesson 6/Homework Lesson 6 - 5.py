# Homework Lesson 6 - 5

grondgetallen = [4, 5, 3, -81]


def kwadraten_som(grondgetallen):
    resultatenSom = 0
    for i in grondgetallen:
        if i > 0:
            resultatenSom += i ** 2
    return resultatenSom


print(kwadraten_som(grondgetallen))
