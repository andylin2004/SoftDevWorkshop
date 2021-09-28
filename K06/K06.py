import random

# reading the file
file = open("occupations.csv", "r")
# where the dictionary will live
occupations = {}
for line in file:
    # remove any new line things
    line = line.strip()
    # we're manually splitting the lines as the default split func doesn't respect the fact that some commas are used in quotes and to be ignored. this is the list for the split components
    splitLine = []
    # this is how we'll respect the commas in quotes. seperate only when comma outside quotes
    quotes = False
    # this will get appended to the list once we get into a comma. in the meantime, this stores all chars that are between commas
    samplingLine = ""
    # looping thru each character in string
    for char in line:
        if char == '"':
            # don't add; just anknoledge that we should ignore commas in terms of splitting until we see another quote
            quotes = not quotes
        elif char == ',' and not quotes:
            # append to splitLine and clear the samplingLine buffer
            splitLine.append(samplingLine)
            samplingLine = ""
        else:
            #add the char
            samplingLine += char
    # add last section after loop ends
    splitLine.append(samplingLine)
    # ignore total and header definitions
    if splitLine[1] != "Percentage" and splitLine[0] != "Total":
        occupations[splitLine[0]] = float(splitLine[1])

# for some reason python freaks out when I force this into the choices thing, so make keys a list to remeady this
keys = list(occupations.keys())
# get weighted probability result
print(random.choices(keys, weights=occupations.values(), k=1)[0])