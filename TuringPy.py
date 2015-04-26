'''python Turing Maschine
'''
class MagnetKopf:

    def __init__(self,band,position):
        self.band = band
        self.position=position

    def moveTo(self,direction):
        if direction == 'r':
            self.position = self.position + 1
        elif direction == 'l':
            self.position = self.position - 1
        else:
            print("error cannot move there")

    def writeToBand(self,symbol):
        self.band[self.position] = symbol

    def readFromBand(self):
        return self.band[self.position]

class Zustand:
    '''Definiert einen Zustand
    '''
    def __init__(self,zustandName):
        '''Constructor
        '''
        self.zustandName = zustandName
        self.actionList = []
        self.activeAction = Action()
        self.isFinal = False
    
    def __str__(self):
        
        return self.zustandName

    def setAction(self, eingabeSymbol, ausgabeSymbol,bewegung,zustand):
        action = Action(eingabeSymbol,ausgabeSymbol,bewegung)
        action.assignState(zustand)
        self.actionList.append(action)

    def getActiveAction(self, inputSymbol):
        for i in self.actionList:
            if i.evaluateInput(inputSymbol):
                self.activeAction = i
                break
    
    def getInputValue(self):
        return self.activeAction.getEingabeSymbol()

    def getWriteValue(self):
       return self.activeAction.getAusgabeSymbol()

    def getBewegung(self):
       return self.activeAction.getBewegung()

    def setFinal(self):
        self.isFinal = True

    def getNextZustand(self):
        return self.activeAction.getState()

    def isFinalState(self):
        return self.isFinal

    def getName(self):
        return self.zustandName
    
    def protocol(self):

        print('Zustand: ', self.getName() )
        print('Eingabe: ', self.getInputValue())
        print('Ausgabe: ', self.getWriteValue())
        print('Bewegung: ', self.activeAction.getBewegung())
        print('Naechster Zustand: ', self.activeAction.getState().getName())
        if self.isFinalState():
            print("Ist finaler Zustand")

class Action:
    '''definiert uebergaenge eines Zustandes
    '''


    def __init__(self,eingabeSymbol='',ausgabeSymbol='',bewegung=''):

        self.eingabeSymbol = eingabeSymbol
        self.ausgabeSymbol = ausgabeSymbol
        self.bewegung = bewegung
        self.zustand = ''

    def setFinal(self):
        self.isFinal = True

    def assignState(self,zustand):
        self.zustand = zustand

    def getState(self):
        return self.zustand

    def evaluateInput(self, inputSymbol):
        if inputSymbol == self.eingabeSymbol:
            return True
        else:
            return False

    def getAusgabeSymbol(self):

        return self.ausgabeSymbol

    def getBewegung(self):

        return self.bewegung

    def getEingabeSymbol(self):
        return self.eingabeSymbol




def main(inputOperation,mode):

    band = []

    for i in range(80):
        band.append('_')

    #inputString = '111_111'
    inputString = inputOperation
    counter = 14

    for i in inputString:
        band[counter] = i
        counter = counter + 1


    #zustaende definieren
    z0 = Zustand("z0")
    z1 = Zustand("z1")
    z2 = Zustand("z2")
    z3 = Zustand("z3")
    z4 = Zustand("z4")
    z5 = Zustand("z5")
    z6 = Zustand("z6")
    z7 = Zustand("z7")
    z8 = Zustand("z8")
    z9 = Zustand("z9")
    z10 = Zustand("z10")
    #eingabev actionen
    z0.setAction("_","_","r",z9)
    z0.setAction("1","_","r",z1)
    z1.setAction("_","_","r",z2)
    z1.setAction("1","1","r",z1)
    z2.setAction("1","_","r",z3)
    z2.setAction("_","_","l",z7)
    z3.setAction("1","1","r",z3)
    z3.setAction("_","_","r",z4)
    z4.setAction("1","1","r",z4)
    z4.setAction("_","1","l",z5)
    z5.setAction("1","1","l",z5)
    z5.setAction("_","_","l",z6)
    z6.setAction("1","1","l",z6)
    z6.setAction("_","1","r",z2)
    z7.setAction("1","1","l",z7)
    z7.setAction("_","_","l",z8)
    z8.setAction("1","1","l",z8)
    #z8.setAction("_","1","r",z0)
    z8.setAction("_","_","r",z0)
    #z9.setAction("1","1","l",z9)
    z9.setAction("1","_","r",z9)
    z9.setAction("_","_","r",z10)
    z10.setFinal()


    magnetKopf = MagnetKopf(band,14)

    currentState = z0
    anzSchritte = 0
    
    while(not currentState.isFinalState()):
        
        symbol = magnetKopf.readFromBand()
        
        currentState.getActiveAction(symbol)

        #currentState.protocol()

        magnetKopf.writeToBand(currentState.getWriteValue())

        magnetKopf.moveTo(currentState.getBewegung())
        anzSchritte += 1
        if (mode == 's'):
            print("\n------------------------------------------------------")
            #print("Gelesenes Symbol:     ", symbol)
            #print("Geschriebenes Symbol: ",currentState.getWriteValue())
            #print("Aktueller Zustand:    ", currentState.getName())
            #print("Wechsle in Zustand:   ", currentState.getNextZustand())
            currentState.protocol()
            print("Anzahl Schritte: ",anzSchritte)
            print("\n------------------------------------------------------")
            s = input('hit enter to continue or e for leaving stepmode\n>>> ')
            if s == 'e':
                mode = 'e'
                
        currentState = currentState.getNextZustand()

        

    stringBand = ''
    for i in band:
        stringBand += i

    print ("\n",stringBand)
    print("\nBenötigte Schritte: ", anzSchritte)

main('111_1111111','s')
