
import time
from math import pi, cos, sin, tan
from random import shuffle, randrange
import breakdown
#test program to spit words back. . .

class spit:
    num = 16
    mindelay = 3
    modedelay = 333



    def fill(self, c, a="+", b="-"):
        self. num = c
        temp = ''
        for i in range(0, c):
                if i %2 == 1:
                    temp += a
                else: temp += b
        print(temp)
        return temp

        #

    def slp(self,  mm,  showTimeStamps=False):
        t = time. ctime()
        m = mm / 100
        time. sleep(m)
        tt = time. ctime()
        if showTimeStamps:  print(t,  " . . " ,  tt)
        # return 1

    def adm(self, ii=1):
        op = ['Accepted', 'conditional', 'deferred', 'declined']
        # r = random.randint(0, len[op])  #make this check stuff later... maybe? lol
        # print( str( op ) )
        r = ''
        rr = 0
        if ii != 1:
            # shuffle( op )
            rr = randrange(4)
            r = op[rr]
        elif ii == 1: r = op[ 0 ]
        else :  r = op[0]
        # print( op )
        return  r, rr
        #spit words with delayed time to
        #read the stream because i ahte reading. . .

    def incrementType(self, ttples, i):
        t = [ ] #reference are magic now...
        ii = 0
        if i < len(ttples) : #the # WARNINGs should go here...
            for l in ttples:
                # print( l )
                anw = l[1]
                ii += 1
                if i == ii: anw += 1
                t.append( (l[0], anw ) )

        return t

#admin test / print admin staatus/fin aid $$$
    def tt(self, msg,  tm,  t):
        ms = msg.split(' ')
        sm = [0, 0 ,0 ,0 , 0]
        # print(str(sm))
        for w in ms:
            rsult, ty = self.adm(11)
            sm[ty] += 1
            sm[len(sm)-1] +=1
            # skl : status"   ##  {: <5}".format(i+1 ) + "...  $:  {:,.2f}".format(s)
            g = " {: <11}".format( w)  + " :  " + str(rsult)
            tempval = 111111/4
            if ty <= 1: g += ' fa${:,.2f}'.format( tempval)
            breakdown.show( g )
            self. slp(t)

        breakdown.show(str(sm))
        return sm

#general timed printer, with new line pause 't' spaces/characters...
    def tp(self, msg,  t=44):
        ms = len(msg) #msg list of words/num/block/wtevr
        breakdown.show(' msg length in chars: ' + str(ms))
        sm = [0, 0]
        # print(str(sm))
        st = 0 #iterator? always puts me to sleep, just keep track of where the last ...
        for i in range(0, ms):
            g = '' + msg[i]
            # g+= str ( msg[i:i+t] )
            if i %t == 0:
                g += ' \n'
            print(g, end=' ')
            self.slp(t, True)
        return sm


    def openFile(self, fn):
        file = open(fn, 'r')
        s = file.read()
        return s

    def printFile(self, f):
        print(f.read())

def deg(rad):
    return rad/pi

def rad(deg):
    return pi * deg/180

def abc(astring): pass
    #take a string, put the 'words' in abc order...

def stoL(astring):
    wd = astring.split(' ')
    rt = []
    for w in wd:
        rt.append( w )
    return rt #list for now.. #made this a string too tho.....



skl = 'CalTech CalSci CMU harveyMudd Cambridge Oxford' #Berkley Cornell Stanford UC CSU Slo Po MIT Hop'
ivish = 'Stanford Harvard Mit Yale princeton Columbia Dude NotreDame Cornel Berkley USC UCLA'
vlginto = "Hi! My name is (rhymes with peachy) and I live in New York City. New videos on my channel every week! I upload vlogs, tech reviews, how-to / behind the scenes travel & lifestyle  "
# prms = [ 1,  2,  3,  5,  7,  11,  17,  23,  37,  47,  57,  67,  79,  83,  91] #. . . ?
# # iniit stuff here but whatever. . .
l = spit()
# # l. slp(10)
a = l. tt(skl,  333,  121 )
a = l.tt(ivish,  333,  221 )
print('   More schools... ')
# a = l. tt(ivish,  333,  51 )
print('   -- College acceptance test -- ')



# l = spit()
# filename = "ee.txt"
# fc = l.openFile(filename)
# breakdown.show('print spit test 33')
# # breakdown.show( fc )
# # l.tp( fc, 22)
# l.tp( stoL(fc) , 22)
# breakdown.show( skl )
# print(fc)
# print( '   ', skl)
# print (a)
