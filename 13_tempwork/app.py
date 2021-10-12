#Team Name: TeamMAN: Andy Lin, Noakai Aronesty, Michael Borczuk
#SoftDev
#K13 --  making our own flask website that also relies on html from K11 and html template found in K12
#2021-10-08

from flask import Flask, render_template
import csv
import random
from pathlib import Path

app = Flask(__name__)

def openFile(totalLine):
    info = {} #create new dict called info
    
    with open(Path(__file__).parent / 'data/occupations.csv',mode='r') as csvfile: #open file for reading; we can refer to it as csvfile
        reader = csv.DictReader(csvfile) #reader is object of class csv
        for row in reader: #every row is a dict; format: {'Job Class': <xx>, 'Percentage': <yy>}
            #for first row in file, create key-value pair in info with format: 'Job Class': <xx>, 'Percentage': <yy>
            #key is 'Job Class'; value is 'Percentage'
            #for every other row, update existing key-value pair to include new value given
            if totalLine or (not totalLine and row['Job Class'] != "Total"):
                info[row['Job Class']] = float(row['Percentage'])

    return info;

def getOccupations():
    info = openFile(True)
    keys = list(info.keys())
    return keys

def getPercentages():
    info = openFile(True)
    values = list(info.values())
    return values

def makeChoice():
    info = openFile(False)
    #make a randomized, weighted choice
    #population are the occupations, weights are the percentages they should show up
    result = random.choices(list(info.keys()), weights = info.values(), k=1)
    stringResult = ''.join(result)
    print(stringResult)
    return stringResult

@app.route("/occupyflaskst")
def job_decider_web():
    jobs = getOccupations()
    percentages = getPercentages()
    return render_template("tablified.html", job = jobs, percentage = percentages, count = len(jobs), result = makeChoice())
    
if __name__ == "__main__":  
    app.debug = True       
    app.run()