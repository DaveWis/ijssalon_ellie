import csv
from helper import *
from presentatie import *

inkomsten = { 
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "waterijsjes-totaal": 750
    }
#som
def som(inkomsten):
    return sum(inkomsten.values())

'''deze som had ik hier nogid om de code goed te laten werken
er ontstond anders een loop tussen helper en boekhouding.py'''
  
#presenteer 
presenteer(inkomsten, som(inkomsten))

with open('boekhouding.csv’, 'w',newline='') as csvfile:     
    for key, value in inkomsten.items():     
    writer = csv.writer(csvfile, delimter=';')     
    writer.writerow([key,value])

