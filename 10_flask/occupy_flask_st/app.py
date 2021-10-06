#Team Name: Hi-C; Yaying Liang Li, Andy Lin, Josephine Lee
#SoftDev
#K10 -- first flask website, serves the outputs of K06's job picker
#2021-10-05

#We tried tinkering with importing the file from K06 to here, but
#it didn't seem to work. End result: we just ctrl c + ctrl v-ied
#it here.

from flask import Flask
import csv
import random

app = Flask(__name__)

def openFile():
    info = {} #create new dict called info
    
    with open('occupations.csv',mode='r') as csvfile: #open file for reading; we can refer to it as csvfile
        reader = csv.DictReader(csvfile) #reader is object of class csv
        for row in reader: #every row is a dict; format: {'Job Class': <xx>, 'Percentage': <yy>}
            #for first row in file, create key-value pair in info with format: 'Job Class': <xx>, 'Percentage': <yy>
            #key is 'Job Class'; value is 'Percentage'
            #for every other row, update existing key-value pair to include new value given
            if row['Job Class'] != "Total":
                info[row['Job Class']] = float(row['Percentage'])

    return info;

def getOccupations():
    info = openFile()
    keys = list(info.keys())
    return keys

def makeChoice():
    info = openFile()
    #make a randomized, weighted choice
    #population are the occupations, weights are the percentages they should show up
    result = random.choices(list(info.keys()), weights = info.values(), k=1)
    stringResult = ''.join(result)
    print(stringResult)
    return stringResult

@app.route("/")
def job_decider_web():
    occupations = getOccupations()
    occupationsString = ""
    for occupation in occupations:
        occupationsString += occupation+"<br>"
    return "Hi-C: Yaying Liang Li, Andy Lin, Josephine Lee <br><br> Possible results:<br>"+occupationsString+"<br><br>"+"Occupation Chosen:<br><br>"+makeChoice()
    
if __name__ == "__main__":  
    app.debug = True       
    app.run()