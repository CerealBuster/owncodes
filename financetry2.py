'''Finance Try2
   jetzt sogar auf git
'''

import urllib.request
import time
import os

#response = ""

#urls = []

#values = []

formatString1 = "| %-13s | %-8s | %-9s | %-8s | %-9s | %-9s |"
formatString2 = "| %-13s | %8s | %9s | %-8s | %9s | %9s |"

def urlDefine():
   #global urls
    urls = []
    name = ['GOOG','YHOO','AAPL']
    for i in range(len(name)):
        urls.append('http://download.finance.yahoo.com/d/quotes.csv?s='+name[i]+
                   '&f=sl1d1t1c1ohgv&e=.csv')
    return urls

def openUrl(url):
    #global response
    response = urllib.request.urlopen(url)
    return response

def getUrlResponse(response):
    #global response
    return response

def readUrl(response):
        #global values
        data = response.read()
        string = data.decode('utf-8')
        string= string.replace("\n",",")
        values =  string.split(',')
        return values

def printHeader():
    print("S T O C K  F E T C H E R")
    print("=========================================================================")
    print(formatString1 %("Stock Name:","Time:","Price:","Change:","Bid:","Ask:"))
    print("_________________________________________________________________________")

def printValuesOnScreen(values):
        #print("| "+values[0]+"      | "+values[3]+"| "
         #     +values[1]+"| "+values[4]+"| "+values[6]+
         #     "| "+values[7]+"|")
        print(formatString2 %(values[0],values[3],
                                                       values[1],values[4],
                                                       values[6],values[7]))
def printFooter():
    print("_________________________________________________________________________")


def run():
    #printHeader()
    url = urlDefine()
    for x in range(10):
        printHeader()
        for i in range(len(url)):
            response = openUrl(url[i])
            values = readUrl(getUrlResponse(response))
            printValuesOnScreen(values)
        printFooter()
        time.sleep(60)
        os.system('cls')
        
if __name__ == "__main__":
    run()
