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

    testout = "What is the adrs of your instn?"
    file = open("test.txt", 'r')
    s = str(file.read())
    words = s.split(" ");
    print(words)
    checkRules(words)


def checkRules(words):
        vowels = ["a","e", "i", "o","u"]
        #print(words[4])
        output = []
        for w in words:
            if len(w) > 4 :
                check = w[1:int(len(w)-2)]  #don't remove first/last char
                print("checking: " + check)
                alteredword = ""
                for v in vowels:
                    print("Checking Vowel: " + v + " check:" + check)
                    if v in check : #scan for vowels
                        alteredword = check.replace(v, '')
                        check = alteredword
                fixedword = w[0] + alteredword + w[len(w)-2]
                output.append(fixedword)
                        # print(alteredword)
                for i in range(len(fixedword)-2):
                    c = fixedword[i]
                    next = fixedword[i+1]
                    if c == next : print("found double")
                        # fixedword = fixedword[1:i-2] #+ fixedword[i+1: len(fixedword)-2]

            else: output.append(w)
        print(output)



def test():
    pass





if __name__ == '__main__':
    # config = openFile()
    # //f = printFile(config)
    readInput()
