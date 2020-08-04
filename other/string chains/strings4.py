# Saul Castro
# Hiralben Hirpara


# config file format
import random

def openFile():
    file = open("test.txt", 'r')
    return file

def printFile(f):
    print(f.read())

def readInput():

    testout = "CarpenteRatcheThread"
    file = open("test.txt", 'r')
    s = str(file.read())
    words = s.split(" ");
    # print("Expected Output: " + testout)
    for w in words:
        if w == '\n': words.remove(w)
    print(words)
    testWords(words,  True)
    # makeChains(words)


def testWords(words, showChecks=False):
    if showChecks:  print(" testing chatbot  ")
    for w in words:
        print( w )
    sen = []
    for i in range(0, len(words) ):
        sen. append( words[i])
        for j in range(0, len(words) ):
            sen. append( words[j]+" "+ words[i])
            # showlist(w,  True)
            # print(i,  " : ", words[i])
            # print(" ", words[j],  words[i])
    if showChecks:
        print(sen )  #raw data
        st = listtoString(sen,  " ") #data only
    print(st)   #show it

# list to string with sep 'char'
def listtoString(   lst, sep):
    s = ""
    for c in lst: s += str(c) + sep
    return s


# string to list, count
def showlist(  li, showChecks=False):
    w = li.split(" ");
    print(w)
    i = 0
    for s in li:
        i +=1
        if showChecks:  print(i,  ":  ",  s)
    return w, i

def makeChains(words, showChecks=False):
    chain = []
    wordcheck = []
    for i in range(0, len(words) ):
        # print(i )
        se = [False, False] #used as start word, end word
        wordcheck.append(se)


    for i in range(0, len(words) ):
        if showChecks:  print(str(i) + " - " + words[i] )
        aword = words[i]
        for j in range(i+1, len(words) ):
            #check the rest of the words for matching links
            bword = words[j]
            if showChecks:  print("   " + str(j) + " ~ " + bword )
            if wordcheck[j][0] == False and wordcheck[j][1] == False:
                temp = checkLinks(aword, bword)
                if showChecks:  print("Check state: " + str(temp) )
                if temp == 1:   #word have not been swapped
                    wordcheck[i][0] = True
                    wordcheck[j][1] = True

                    chain.append(aword)
                    chain.append(bword)
                elif temp == 2: #words have been swapped, swap flag indexes to match.
                    wordcheck[j][0] = True
                    wordcheck[i][1] = True
                    chain.append(bword)
                    chain.append(aword)

    print(chain)
    # k = 0
    # for i in  wordcheck:
    #     print("word check: " + str(i) + " = "+  words[k] )
    #
    #     k+= 1

# compare words, return 0 for no match,
# 1 if end of a == start of b
# 2 if end of b == start of a
def checkLinks(a, b):
    print("      " + a + " " + b)
    s , e = getEnds(a)
    ss , ee = getEnds(b)
    if e == ss :
        return 1
    elif s == ee:
        return 2
    return 0
    # st = "start: " + s + " end:" + e
    # print("end" + st)


def getEnds(word):
    st = word[0]
    ed = word[len(word)-1]

    return st, ed



if __name__ == '__main__':
    readInput()
