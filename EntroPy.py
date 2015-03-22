"""
    Dieses modul berechnet entropie von files

"""


import argparse
import math
parser = argparse.ArgumentParser()

parser.add_argument("inputFile",type=str, help="Path to the Inputfile")
parser.add_argument("-o", "--OutputFile", type=str, help="Output File")
args = parser.parse_args()

class Character:
    occurence = 0
    probability = 0.0
    information = 0.0
    
    def __init__(self, occurence):
        self.occurence = occurence
        
def openFile(fileName):
    #versuche das outputfile zu oeffnen
    try:
        file = open(fileName,'r')
        return file
    except IOError:
        print("cannot open", args.inputFile)
        return 0


def computeProbability(dictionary):
    print("Computing probabilitys...")
    
    for i in dictionary.values():
        i.probability = i.occurance /amountOfCharacters

def computeInformation(dictionary):
    
    for i in dictionary.values():

          i.information = math.log2(1/i.probability)
          
def computeEntropy(dictionary):
    summe = 0
    for i in dictionary.values():
        
        summe += i.information * i.probability

def getDataFromFile():

def run():  
    #Variables
    characters = {}
    amountOfCharacters = 0
    file = openFile(args.inputFile)

    while True:
        c = file.read(1)
        if( c in characters):
            #illustratorisch #schneller wäre characters[x].occurance
            temp = characters.get(c)
            temp.occurance +=1
        else:
            characterObject = Character(1)
            characters[c] = characterObject
    
        amountOfCharacters += 1

    

if __name__ == "__main__":
    run()
                             
