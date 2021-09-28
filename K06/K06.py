import random

file = open("occupations.csv", "r")
occupations = {}
for line in file:
    newLine = line.strip()
    splitLine = newLine.split(",")
    occupations[splitLine[0]] = splitLine[1]

print(occupations)