# Homework Lesson 10 - 2

import random

def monopolyworp():
  dubbeleWorpen = 1
  magNogGooien = True

  while magNogGooien:
    worp1 = random.randrange(1,6)
    worp2 = random.randrange(1,6)

    if worp1 == worp2 and dubbeleWorpen == 3:
      print(str(worp1) + " + " + str(worp2) + " = " + str(worp1+worp2) + " (Naar de gevangenis met jou, schavuit!)")
      magNogGooien = False

    elif worp1 == worp2:
      print(str(worp1) + " + " + str(worp2) + " = " + str(worp1+worp2) + " (Dubbel)")
      dubbeleWorpen = dubbeleWorpen + 1

    else:
      print(str(worp1) + " + " + str(worp2) + " = " + str(worp1+worp2))
      magNogGooien = False

monopolyworp()
