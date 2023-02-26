# Spy Game: Data Encoding/Decoding
# King Jones-Frazier
# w214697414@student.hccs.edu


from datetime import date
slash       = chr(47)
bslash      = chr(92)
dquote      = chr(34)
squote      = chr(39)
rejection   = "+-=@#$%^&*()_[]{}|<>`~" + dquote   + squote + bslash + slash
sentinel    = "EOD"

"""

 my functions and global variables
-------------------------------------------------------------------------------
"""

today = date.today()
uStringLst=[]
uString = ""
key = ""
oldWord = ""
indexOW = 0

def kioskFunct():
    exit = False
    while exit == False:
        print("========================================")
        print("Spy game: Data Encryption")
        print("Encrption Operator: John Doe")
        print("Operator ID: 132456789")
        print(f"Date: {today}")
        print("========================================")
        print("")
        print("")
        print(". . . . . . . . . . . . . . . . . . . . ")
        print("Encoding and Decoding Kiosk")
        
    

        path = getDecision(1)

        if path =="e":
            global key
            

            getPhrase()
            getKey()
            uStringLst = build_word_list(uString)
            print_list(uStringLst)
            editString(uStringLst)
            encLst(uStringLst,key)
            #do you want to quit in get decision 4
            path = getDecision(4)
            if path == 1:
                exit = True
            elif path == 2:
                print(" ")
                print("returning to start screen...")
                print(" ")
                kioskFunct()
            else:
                print("please put 1 for yes or 2 for no")

        elif path == "d":
            getPhrase()
            getKey()
            uStringLst = build_word_list(uString)
            print_list(uStringLst)
            decLst(uStringLst,key)
            
            

        else:
            if (path != "e") or (path != "d"):
                print("please enter either e to encode or d to decode")
                print(path != "d")
                print(path != "e")
                kioskFunct()
    
def getKey():
    print("==========")
    print(" ")
    global key
    key = input("Whats the key: ")
    print("==========")

def getPhrase():
    print("")
    print(". . . . . . . . . .")
    global uString
    uString = str(input("Enter your string:"))
    #print("uString is", uString)
    print(" ")
    print(". . . . . . . . . .")

def editString(myString):
    print("")
    print(". . . . . . . . . .")
    global oldWord
    path = getDecision(2)
    #print("path = ", path)
    #1 = yes 2 = no
    if path == 1:  #to delete a word
        oldWord = input("Which word would you like to change?")
        if oldWord in myString:
            print(f"removing {oldWord} from {myString}")
            indexOW = myString.index(oldWord)
            #print("index of oldWord", indexOW)
            myString.remove(oldWord)
            printStr(myString)
            
            
            
            insWord(indexOW,myString) #insert word function
            

    elif path == 2: #doesn't want to replace
        print("Will proceed normally...")

    else: #input something other than 1 or 2
         print("Please select either (1)Yes or (2)No")
         editString(myString)

def insWord(oWordIndx,myString):
    print("")
    print(". . . . . . . . . . .")
    #global oldWord
    path = getDecision(3) #ask to replace word

    if path == 1:
        #indexOW = myString.index(oWord)
        newWord = input("What word would you like to put? " )
        myString.insert(oWordIndx,newWord)
        
    elif path == 2:
        print("we'll leave it like that")
    else: #input something other than 1 or 2
        print("Please select either (1)Yes or (2)No")
        insWord(indexOW,myString)  
    
    printStr(myString)
    print(". . . . . . . . . .")
    print("")
#called by kioskfunction
def getDecision(path):
    print("")
    #path 1
    if path == 1:
        decision = input("Do you want to encode(e) or decode(d):")
        decision.lower()
        print("")
        return decision

    #path 2
    elif path == 2:
        decision = int(input("Would you like to edit the string.(1)yes or (2)no: "))
        print("")
        return decision

    #path 3 called in editString
    elif path == 3:
        decision = int(input("Would you like to replace the old word? (1)yes or (2)no: "))
        print("")
        return decision
    #path 4 called in kioskfunct
    else:
        decision =  int(input("Do you want to quit? (1)yes or (2)no: "))
        print("")
        return decision

def encLst(myLst, key):
    print("")
    enc_lst = []
    for i in myLst:
        #print('i is:', i)
        enc_lst.append(encode_word(i, key))
        #print("enc_lst is:",enc_lst)
    printStr(enc_lst)    
    print_list(enc_lst)
    print("")
    #return enc_lst  

def decLst(myLst, key):
    print("")
    dec_lst = []
    for i in myLst:
        #print('i is:', i)
        dec_lst.append(decode_word(i, key))
        #print("dec_lst is:",dec_lst)
    printStr(dec_lst)    
    print_list(dec_lst)
    print("")
    #return dec_lst  

def printStr(myString):
    print("")
    uStr = ""
    for i in myString:
        uStr += " "
        uStr += i
        uStr += " "
    print("The phrase is", uStr)
    print("")


def key_offset(key):
    offset = 0
    for letter in key:
        offset += ord(letter)
    return offset

def words_in_string(parse):
    
    wordcount   = int(0)
    currentword = ""
    delimiters  = " ,.;:!?"
    inword      = False
    error       = False
    count       = 0
    length      = len(parse.strip())
    wordpack    = ""

    
    for i in range(length):
        
        char = parse[i]
#print(char)
    
        if char in delimiters:
            
# check to see if inword
#print(f"Delimeter :{char}: found at index {i}.")
            if inword:
                
# current word completed
#print(f"Current word completed: detected at index {i}, {currentword}, current word count is {wordcount}")
                inword = False
                wordpack += currentword + "\n"
                currentword = ""
            else:
                # not in a word ignore delimiter
                #print(f"Delimeter :{char}: found in whitespace.")
                pass
        elif inword:
            #keep building current wordcount
            
            currentword = currentword + char
        else:
            #start word
            wordcount   += 1
            currentword = char
            inword      = True
#print(f"New word found: at index {i}, {currentword}, current wordcount is {wordcount}")
    if inword:
# pack the last remaining wordcount
        
        wordpack += currentword
    
    return wordcount

def extract(parse, index):
    
    wordcount   = 0
    currentword = ""
    delimiters  = " ,.;:!?"
    inword      = False
    error       = False
    count       = 0
    length      = len(parse.strip())
    wordpack    = ""
    num = words_in_string(parse)
    if index > num:
        return "Error: You cannot request more words that the string contains."
    for i in range(length):
        char = parse[i]
        if char in delimiters:
# check to see if inword
            if inword:
# current word completed
                if index == wordcount:
# found the requested word
                    return currentword
                inword      = False
                wordpack    += currentword + "\n"
                currentword = ""
            else:
# not in a word ignore delimiter
                pass
        elif inword:
#keep building current wordcount
            currentword = currentword + char
        else:
#start word
            wordcount   += 1
            currentword = char
            inword      = True
    if inword:
# pack the last remaining wordcount
        wordpack += currentword
        if index == wordcount:
# found the requested word
            #print("current word is",currentword)
            return currentword


def build_word_list(mystring):
    
    mylist = []
    error  = True
    num = words_in_string(mystring)
    for i in range(1, num + 1):
        word = extract(mystring, i)
        l    = len(word)
        
        if word == "EOD":
            print("End of Data (EOD) found as a word. String has the appropriate sentinel value. Processing may begin.")
            error = False
            break
        
        elif word!="EOD" and i== num +1:
                
                print("Syntax Error: Your message did not have the end-of-data sentinel.")
                return []
        else:
            mylist.append(word)
   
    return mylist






def print_list(mylist):
    count = 1
    for item in mylist:
        print(f"{count}: {item}")
        count += 1

def encode_word(word, key):
    offset = key_offset(key)
    length = len(word)
    build  = ""
    for char in word:
        val      = ord(char)
        div      = (0 + length) // 26 + 1  # Number of times it would wrap the alphabet
        div      = 1
        shift    = (offset + length) % 26
        if 65 <= val <= 90:                             # Upper case
            if val + shift <= 90:
                new_ord  = val + shift
            else:
                new_ord  = (val + shift  - 91) + 65
        elif 97 <= val <= 122:                             # Lower case
            if val + shift  <= 122:
                new_ord  = val + shift
            else:
                new_ord  = (val + shift  - 123) + 97
        else:
            new_ord = ord(char)
        new_char = chr(new_ord)
        build = build + new_char
    return build

def decode_word(word, key):
    offset = key_offset(key)
    length = len(word)
    build  = ""
    for char in word:
        val      = ord(char)
        div      = (0 + length) // 26 + 1  # Number of times it would wrap the alphabet
        div      = 1
        shift    = (offset + length) % 26
        if 65 <= val <= 90:                             # Upper case
            if val - shift >= 65 :
                new_ord  = val - shift
            else:
                new_ord  = (val - shift - 65) + 91
        elif 97 <= val <= 122:                             # Lower case
            if val - shift >= 97:
                new_ord  = val - shift
            else:
                new_ord  = (val - shift - 97) + 123
        else:
            new_ord = ord(char)
        new_char = chr(new_ord)
        build = build + new_char
    return build

kioskFunct()

print("Thank you for using corner street encoder. Good bye.")
