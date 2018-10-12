# Homework Lesson 9 - 3

studentenResultaten = {
  "Gerard":8.3,
  "Henk":9.1,
  "Lotte":9.5,
  "Dirk":4.5,
  "Jan":9.8,
  "Gert-Jan":9.7,
  "Bert":9.0,
  "Kevin":1.0,
  "Sanne":4.3,
  "Eline":5.5
}

for key in studentenResultaten:
  if float(studentenResultaten[key]) >= 9.0:
    print(key + " had een " + str(studentenResultaten[key]))
