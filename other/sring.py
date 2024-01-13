# Saul Castro
# Hiralben Hirpara


# config file format
# <num-servers>
# • <num-neighbors>
# • <server-ID> <server-IP> <server-port>
# • <server-ID1> <server-ID2> <cost>
# todo class type for server, id, ip, port, costtoserver1


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
    print("Expected Output: " + testout)
    for w in words:
        if w == '\n': words.remove(w)
    print(words)
    makeChains(words)


def makeChains(words):
    chain = []
    wordcheck = []
    for i in range(0, len(words) ):
        print(i )
        se = [False, False] #used as start word, end word
        wordcheck.append(se)


    for i in range(0, len(words) ):
        print(str(i) + " - " + words[i] )
        aword = words[i]
        for j in range(i+1, len(words) ):
            #check the rest of the words for matching links
            bword = words[j]
            print("   " + str(j) + " ~ " + bword )
            if wordcheck[j][0] == False and wordcheck[j][1] == False:
                if checkLinks(aword, bword) :
                    chain.append(aword)
                    chain.append(bword)
                    if aword == words[i]:
                        wordcheck[i][0] = True
                        wordcheck[j][1] = True
                    else:
                        wordcheck[j][0] = True
                        wordcheck[i][1] = True



    print(chain)
    for i in  wordcheck:
        print("word check: " + str(i))

def checkLinks(a, b):
    print("      " + a + " " + b)
    s , e = getEnds(a)
    ss , ee = getEnds(b)
    if e == ss :
        return a, b
    elif s == ee:
        return b, a
    # st = "start: " + s + " end:" + e
    # print("end" + st)


def getEnds(word):
    st = word[0]
    ed = word[len(word)-1]

    return st, ed



if __name__ == '__main__':
    readInput()
