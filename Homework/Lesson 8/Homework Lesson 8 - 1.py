# Homework Lesson 8 - 1

def seizoen(maand):
    if 1 <= maand <= 2 or maand == 12:
        return "Winter"
    elif 3 <= maand <= 6:
        return "Lente"
    elif 6 <= maand <= 8:
        return "Zomer"
    elif 9 <= maand <= 11:
        return "Herfst"

print(seizoen(1))