'''
create file called output_keys.txt
sort the tv shows according to number of seasons
shows with same number of seasons separated by semi colons

create file called output_titles.txt
sort in alphabetical order

open file for writing
f = open('myfile.txt', 'w') 'r'= reading, 'w'=writing 'a'=appending
f.write(str(num1))

# Open a file for reading and appending
with open('myfile.txt', 'r+') as f:
    # Read in two integers
    num1 = int(f.readline())
    num2 = int(f.readline())

The most common methods to read text from a file are file.read() and file.readlines().
The file.read() method returns the file contents as a string. 
The file.readlines() method returns a list of strings, where the first element is the contents of the first line, 
the second element is the contents of the second line, and so on.

method
create a list. compare each item 1 at a time to another list to find a match.
then add the value of the match to another list to be added to the dictionary
'''

f = open('file1.txt', 'r')
tvShows = f.readlines()


dictItems = []
showlst = {}
showDict = {}
for i in range(0,(len(tvShows)-1),2):
    showlst[tvShows[i+1]]= int(tvShows[i].strip())
    showDict[tvShows[i]] = tvShows[i+1]

theKeys = list(showDict.keys())
check = 0
for show in showlst:
    for i in range(len(theKeys)):
        listing = showlst.get(show)
        match = (listing == int(theKeys[i]))
        if match:
            check +=1
    
        
'''
for i in range(len(showlst)):
    if showlst[i] == theKeys[i]:
            showDict[theKeys[i]]= []
'''
#print('showlst:',showlst)