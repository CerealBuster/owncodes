#!/usr/bin/env python
"""Programm: Finance Try2
   Version 0.3
   Author: CerealBuster
   Beschreibung: Dieses Programm holt Stockdaten von Yahoo.
"""

import urllib.request
import time
import os
import sys

#Variabeln

formatString1 = "| %-13s | %-8s | %-9s | %-8s | %-8s | %-9s | %-9s |"
formatString2 = "| %-13s | %8s | %9s | %8s | %4s | %9s | %9s |"


def urlDefine():
    """
    Definiert die Url zu der Aktie
    return: urls array
    """
    urls = []
    name = ['GOOG','YHOO','AAPL']
    for i in range(len(name)):
        #Diese Url koentte in zuckunft aendern
        urls.append('http://download.finance.yahoo.com/d/quotes.csv?s='+name[i]+
                   '&f=sl1d1t1c1p2abohgv&e=.csv')
    return urls

def openUrl(url):
    """
    Oeffnet eine Url und gibt die response zurueck
    return: response object
    """

    response = urllib.request.urlopen(url)
    return response

def getUrlResponse(response):
    """
    gibt die response einer Url zurueck
    return: response object
    """
    return response

def readUrl(response):
    """
    Wandelt die Response in einen String um
    return: values array
    """

    data = response.read()
    string = data.decode('utf-8')
    string= string.replace("\n",",")
    values =  string.split(',')
    return values

def printHeader():
    """
    Schreibt den Header in die Konsole
    """
    print("S T O C K  F E T C H E R")
    print("======================================================================================")
    print(formatString1 %("Stock Name:","Time:","Price:","Change:","%:","Bid:","Ask:"))
    print("______________________________________________________________________________________")

def printValuesOnScreen(values):
    """
    Schreibt die Daten formatiert auf die Konsole
    
    """
    print(formatString2 %(values[0],values[3],values[1],values[4],values[5],values[7],
                          values[6]))
def printFooter():
    """
    Schreibt den Footer auf die Konsole
    """
    print("______________________________________________________________________________________")

def clearScreen():
    """
    Loescht die Konsolenausgabe 
    """
    if (sys.platform == 'linux'):
        os.system('clear')
    elif(sys.platform == 'windows'):
        os.system('cls')
    else:
        pass
    

def run():
    """
    Main Methode 
    """
    #url definieren
    url = urlDefine()
    #Header und stokdaten abarbeiten
    for x in range(10):
        printHeader()
        for i in range(len(url)):
            response = openUrl(url[i])
            values = readUrl(response)
            printValuesOnScreen(values)
        printFooter()
        #refresch nur jede Minute (kann ev bald als inputparam angegeben werden)
        time.sleep(60)
        clearScreen()
        
if __name__ == "__main__":
    run()
u
