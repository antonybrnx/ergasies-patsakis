import urllib.request
import json
from datetime import date
from prettytable import PrettyTable

input('Πατήστε enter για να τρέξει ')
print('running...')

def getHtmlData(url):
    r  = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode()
    data = json.loads(html)
    return data

def makeNewDrawList():
    numberList = []
    for i in range(1,81):
        numberList.append([i,0])
    return numberList

myTable = PrettyTable(["Mera", "Arithmos"]) # ftiaxnei pinaka gia tin teliki emfanisi twn arithmwn
today = date.today()
month = today.month
month = '0' * (2 - len(str(month))) + str(month)
day = today.day

moreShownNumL = []

for day in range(1,day+1):
    counter = 0
    numberList = makeNewDrawList()
    day = '0' * (2 - len(str(day))) + str(day)
    date = str(today.year) + '-' + month + '-' + day
    url = 'https://api.opap.gr/draws/v3.0/1100/draw-date/{}/{}/draw-id'.format(date,date)
    draws = getHtmlData(url)
    if len(draws) != 0:
        for draw in draws:
            counter+= 1
            url = 'https://api.opap.gr/draws/v3.0/1100/{}'.format(draw)
            results = getHtmlData(url)
            winningNumbers = results['winningNumbers']['list']
            for number in winningNumbers:
                numberList[number-1][1] += 1
        timeShown = numberList[0][1]
        moreShownNum = 0
        for i in range(len(numberList)-1):
            if numberList[i+1][1] > timeShown:
                moreShownNum = numberList[i+1][0]
                timeShown = numberList[i+1][1]
        moreShownNumL.append(moreShownNum)
        myTable.add_row([day, moreShownNum])
    else:
        break
print(myTable)
