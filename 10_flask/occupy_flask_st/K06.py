#Team Name: Hi-C; Yaying Liang Li, Andy Lin, Josephine Lee
#SoftDev
#K06 -- Reading CSV Files
#2021-09-28

#Our program starts by reading the file and removing the new lines off each occupation in the CSV file.
#Because some of the jobs have commas (outside of separating the job and the percentage), we decided to
#manually split the lines. For every line in the file, go through every char in the line, and if we
#see a comma and it's not part of the quoted info, add that value to the temporary storing list.
#if we see a comma and it is within the quotes, don't separate - keep adding the char into our temp.
#storing String. Add info in temp. list to our dictionary, and get weighted choices using random.choices.

#for random.choices, population (list of "choices") and weights (list of the weights
#of these choices) must be of the same list size

import random

def jobDecider():
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
                # don't add; just acknowledge that we should ignore commas in terms of splitting until we see another quote
                quotes = not quotes
            elif char == ',' and not quotes: #we see a comma, and it's not part of the quoted info --> add value to the temporary storing list
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
    result = random.choices(keys, weights=occupations.values(), k=1)[0]
    print(result)
    return result

jobDecider()