# Homework Lesson 6 - 3


def lang_genoeg(lengte):
    if lengte >= 120:
        res = "Je bent lang genoeg voor de attractie!"
    else:
        res = "Sorry, je bent te klein!"
    return res


print(lang_genoeg(160))
