# Homework Lesson 10 - 3

def code(invoerstring):
  finalOutput = ""
  for char in invoerstring:
    charShifted = chr(ord(char) + 3)
    finalOutput = finalOutput + charShifted

  return finalOutput

print(code("RutteAlkmaarDen Helder"))
