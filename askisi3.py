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

myTable = PrettyTable(["Arithmos", "Emfaniseis"]) # ftiaxnei pinaka gia tin teliki emfanisi twn arithmwn
today = date.today()
month = today.month
day = today.day

# list me olous tous pithanous arithmous
numberList = []
for i in range(1,81):
    numberList.append([i,0])

for day in range(1,day + 1):
    month = '0' * (2 - len(str(month))) + str(month) # Prosthetei ena mideniko sto mina an einai monopsifios
    day = '0' * (2 - len(str(day))) + str(day)
    date = str(today.year) + '-' + month + '-' + day

    url = 'https://api.opap.gr/draws/v3.0/1100/draw-date/{}/{}/draw-id'.format(date,date)
    data = getHtmlData(url)
    firstDraw = data[0]

    url = 'https://api.opap.gr/draws/v3.0/1100/{}'.format(firstDraw)
    data = getHtmlData(url)
    winningNumbers = data['winningNumbers']['list']
    for number in winningNumbers:
        numberList[number-1][1] += 1

print('\nΣτατιστικά:')
for i in range(1,81):
    myTable.add_row([i, numberList[i-1][1]])

print(myTable)
