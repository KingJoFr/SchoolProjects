import csv

freqDict = {}
itemsLCase = []
with open('input1.csv', 'r') as csvfile:
    items = csv.reader(csvfile, delimiter =',')
    
    for row in items:
        for word in row:
            count = row.count(word)
            freqDict[word] = count

for word in freqDict:
    print(word, freqDict[word])

