# Saul Castro
# Hiralben Hirpara


# config file format
# read plain text file
# filter vowels and repeated chars for latin/english
# to addon:
# command pop + inital arguments
# open parser

import argparse
import sys

class ReadConfig():
    val = "" #store the data/args to be parsed
    def __init__(self, v="No data"):
        if v == "": pass
        else:  self.val = v

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



    def getCommandArgs(self,  printInfo = True):
        try:
            parser = argparse.ArgumentParser()
            args = parser.parse_args()
            print (sys.argv)
            i = 0
            for w in words:
                # split and process input for chainable operators
                print ("  " ,i, w)
                i+=1
            return str(v)
            for a in args:
                print ("  " ,i, a)
                # print (sys.argv[1])
                return 0
        except:
            print("__sys_Message: ")
            e = sys.exc_info()[0]
            print(e)
        else: print("Command arg check done with else?")
        print("Command arg check done.")

    # ====================== +++++++++++++++++++++
    def addCommandArgExample(self):
            # https://stackoverflow.com/questions/70797/user-input-and-command-line-arguments
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument("square", help="display a square of a given number",
                    type=int)
            args = parser.parse_args()
            #print all the sys argument passed from cmd line including the program name.
            print (sys.argv)
            #print the second argument passed from cmd line; Note it starts from ZERO
            print (sys.argv[1])
        except:
            # e = sys.exc_info()[0]
            print(e)
    # ====================== +++++++++++++++++++++
    # ====================== +++++++++++++++++++++
    # ====================== +++++++++++++++++++++
    def readInput(self):
        print("reading Input . . . ")
        print(" careful what you ask . . . ")
        v = input()
        words = v. split(' ')
        i = 0
        for w in words:
            # split and process input for chainable operators
            print ("  " ,i, w)
            i+=1
        return str( v )


    # def getParams(self):
    #     readInput()


    def test():
        pass
        # self. getCommandArgs()





if __name__ == '__main__':
    # config = openFile()
    # //f = printFile(config)
    rc = ReadConfig()
    rc. readInput()
