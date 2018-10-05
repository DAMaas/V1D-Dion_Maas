# Homework Lesson 8 - 4

studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    gemiddelden = []
    for list in studentencijfers:
        gemiddelden.append(sum(list) / 3)
    return gemiddelden

def gemiddelde_van_alle_studenten(studentencijfers):
    gemiddelden = []
    gemiddeldenIedereen = 0
    for list in studentencijfers:
        gemiddelden.append(sum(list) / 3)
    gemiddeldenIedereen = sum(gemiddelden) / 4
    return int(gemiddeldenIedereen)

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))
