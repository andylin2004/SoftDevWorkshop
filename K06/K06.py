import random

file = open("occupations.csv", "r")
occupations = {}
for line in file:
    line = line.strip()
    splitLine = []
    quotes = False
    samplingLine = ""
    for char in line:
        if char == '"':
            quotes = not quotes
        elif char == ',' and not quotes:
            splitLine.append(samplingLine)
            samplingLine = ""
        else:
            samplingLine += char
    splitLine.append(samplingLine)
    if splitLine[1] != "Percentage" and splitLine[0] != "Total":
        occupations[splitLine[0]] = float(splitLine[1])

# for some reason python freaks out when I force this into the choices thing
keys = list(occupations.keys())
print(random.choices(keys, weights=occupations.values(), k=1)[0])