import random

file = open("occupations.csv")
occupations = {}
for line in file:
    splitLine = line.split(",")
    occupations[splitLine[1]].append(splitLine[2])