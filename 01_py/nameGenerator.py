# Andy Lin
# SoftDev
# K01 -- random student selector but without the actual student names
# 2021-09-21


from random import randrange

def openNameFile():
    file = open("nameList.txt", "r")
    fileLines = []
    for line in file:
        fileLines.append(line)
    return fileLines

fileLines = openNameFile()
input = input("Input a number for a student, or enter for a random")
if input.isnumeric() and input != "0":
    print(fileLines[int(input)])
else:
    print(fileLines[randrange(len(fileLines))])