"""
    Dieses modul berechnet entropie von files

"""


import argparse
import math


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

def closeFile(fileName):
    try:
        fileName.close()
    except IOError:
        print("Cannot close file")
    
def computeProbability(dictionary, amountOfCharacters):
    print("Computing probabilitys...")
    
    for i in dictionary.values():
        i.probability = i.occurence /amountOfCharacters
    return dictionary

def computeInformation(dictionary):
    print("Computing information...")
    
    for i in dictionary.values():

          i.information = math.log2(1/i.probability)
    return dictionary
          
def computeEntropy(dictionary):
    print("Computing entropy...")
    entropy = 0
    for i in dictionary.values():
        
        entropy += i.information * i.probability
    return entropy

def printResults(dictionary, amountOfCharacters, entropy):
    formatString = " |{0:<6}|{1:<15}|{2:<15}|{3:<20}|"
    formatString2 = " |{0:6}|{1:15}|{2:15}|{3:20}|"
    
    print("Character types in file: ", len(dictionary))
    print("Number of characters in file: ", amountOfCharacters)
    print("Entropy of file: ", entropy)
    print("")
    print(formatString.format("Char: ","Occurance: ","Probability: ","Information:"))
    
    for i,j in dictionary.items():
          
          print(formatString2.format(i, j.occurence, j.probability, j.information))
    

def printToFile(inputFileName,fileName,dictionary,amountOfCharacters,entropy):
    formatString = " |{0:<6}|{1:<15}|{2:<15}|{3:<20}|"
    formatString2 = " |{0:6}|{1:15}|{2:15}|{3:20}|"
    try:
        file = open(fileName,'a+')
        string = "Results for: "
        file.write(string)
        file.write(inputFileName)
        file.write("\n\n")
        string = "Character types in file: "
        file.write(string)
        file.write(str(len(dictionary)))
        file.write("\n")
        string = "Number of characters in file: "
        file.write(string)
        file.write(str(amountOfCharacters))
        file.write("\n")
        string = "Entropy of file: "
        file.write(string)
        file.write(str(entropy))
        file.write("\n")
        file.write(formatString.format("Char: ","Occurance: ","Probability: ","Information:"))
        file.write("\n")
    
        for i,j in dictionary.items():
          
              file.write(formatString2.format(i, str(j.occurence), str(j.probability), str(j.information)))
              file.write("\n")
        file.write("\n\n")
        file.close()
        print("wrote results for: ",inputFileName)
    except IOError:
        print("ERROR: could not Create file\n")

    

   
    
     

def batchMode():
    print("notImplementedjet")

def normalMode():
    print("notImplementedJet")


def run():
    
    parser = argparse.ArgumentParser()
    #parser.add_argument('inputfile', nargs='+', type=argparse.FileType('r'), help='name of the input Files')
    parser.add_argument("inputFile",type=str, nargs='+',help="Path to the Inputfile")
    parser.add_argument("-o", "--OutputFile", type=str, help="Output File")
    args = parser.parse_args()
    
    print("======================================================")
    print("Starting ComputeMain....")
    for inputFile in args.inputFile:
        #Variables
        characters = {}
        amountOfCharacters = 0
        entropy = 0
        file =openFile(inputFile)
        print("Reading file " ,inputFile)
        while True:
            c = file.read(1)
            if(not c):
                break
            if( c in characters):
                #illustratorisch #schneller wäre characters[x].occurance
                temp = characters.get(c)
                temp.occurence +=1
            else:
                characterObject = Character(1)
                characters[c] = characterObject
    
            amountOfCharacters += 1
    
        characters = computeProbability(characters, amountOfCharacters)
        characters = computeInformation(characters)
        entropy = computeEntropy(characters)
        printResults(characters, amountOfCharacters,entropy)
        if(args.OutputFile):
            printToFile(inputFile,args.OutputFile,characters,amountOfCharacters,entropy)

        closeFile(file)
        print("Done.")
        print("======================================================")

if __name__ == "__main__":
    run()
                             
