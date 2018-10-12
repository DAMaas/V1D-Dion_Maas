# Homework Lesson 9 - 4

def ticker(filename):
  tickerDictionary = {}

  fileData = open(filename + ".txt")
  fileDataLines = fileData.readlines()

  for line in fileDataLines:
    (key, value) = line.split(":")
    strippedValue = value.rstrip('\n')
    tickerDictionary[key] = strippedValue
  return tickerDictionary

tickerDictionary = ticker("TickerList")

companyName = input("Enter company name: ")
for key, value in tickerDictionary.items():
  if key == companyName:
    print("Ticker symbol: " + value)

tickerSymbol = input("Enter ticker symbol: ")
for key, value in tickerDictionary.items():
    if value == tickerSymbol:
        print("Company name: " + key)
