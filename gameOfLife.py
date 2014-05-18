import random
import tkinter

def calculateStatus(array,x,y):
    '''Berechnet den status der naechsten generation
    '''

    nachbarn = 0
    status = False
    # oben
    if (((y-1) >= 0) and (array[x][y-1] == True)):
         nachbarn +=1
    # unten
    if (((y+1) <= len(array[x])-1) and (array[x][y+1] == True)):
        nachbarn +=1

    # rechts
    if (((x+1) <= len(array)-1) and (array[x+1][y] == True)):
         nachbarn +=1

    # links
    if ( ((x-1) >= 0) and (array[x-1][y] == True)):
         nachbarn +=1

    # rechts unten
    if (((x+1) <= len(array) -1) and ((y+1) <= len(array[x])-1 )
                              and (array[x+1][y+1] == True)):
        nachbarn += 1
    # links oben
    if (((x-1) >= 0) and ((y-1) >= 0)
                              and (array[x-1][y-1] == True)):
        nachbarn +=1
    # rechts oben
    if (((x+1) <= len(array) -1 ) and ((y-1) >= 0)
                              and (array[x+1][y-1] == True)):
         nachbarn +=1
    # links unten
    if (((x-1) >= 0) and((y+1) <= len(array[x])-1)
                              and (array[x-1][y+1] == True)):
         nachbarn +=1
         
         
    if (nachbarn < 2):
        status = False
    if ((nachbarn == 2 or nachbarn ==3) and array[x][y] == True):
        status = True
    if ((nachbarn == 3 and array[x][y] == False)):
        status = True
    if (nachbarn > 3 ):
        status = False
    return status

def defineWorld(i):
    '''Creates a random world with the height and width of i
    '''
    array = []
    innerArray = []
    status = 0
    for x in range(i):
        for y in range(i):
            status = random.randrange(2)
            if (status == 0):
                innerArray.append(False)
            else:
                innerArray.append(True)

        array.append(innerArray)
        innerArray = []
    return array

def calculateGeneration(array):
    '''Calculates the next generation of the world
    '''
    oldArray = array
    newArray = []
    newInnerArray = []
    status = False
    for x in range(len(oldArray)):
        for y in range(len(oldArray[x])):
            status = calculateStatus(oldArray,x,y)
            newInnerArray.append(status)
        newArray.append(newInnerArray)
        newInnerArray = []
    return newArray
    

def printWorld(array):
    '''prints world to the command prompt
    '''
    world = array
    line = ''
    for i in world:
        for x in i:
            if (x == True):
                line += '#'
            else:
                line += '-'
        print(line)
        line = ''
        
def gaficWorld():
    '''TODO
    '''
    
def main():
    array = defineWorld(50)
    for i in range(50):
        array = calculateGeneration (array)
        printWorld(array)
        print(' ')
        print('Generation: ', i)
        



    
