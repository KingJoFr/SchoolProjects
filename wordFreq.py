import csv

freqDict = {}
itemsLCase = []
with open('input1.csv', 'r') as csvfile:
    items = csv.reader(csvfile, delimiter =',')
    
    for row in items:
        for word in row:
            word1 = word.lower()
            itemsLCase.append(word1)
    for word in itemsLCase:
        count = itemsLCase.count(word)
        freqDict[word] = count

print(freqDict)

