
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
        if ii != 1:
            # shuffle( op )
            rr = randrange(2)
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

    def tt(self, msg,  tm,  t):
        ms = msg.split(' ')
        sm = [ ('Accepted', 0), ('conditional', 0), ('deferred', 0), ('declined', 0) ]
        # print(str(sm))
        for w in ms:
            rsult, ty = self.adm(0)
            sm = self.incrementType(sm, ty)
            # skl : status"   ##  {: <5}".format(i+1 ) + "...  $:  {:,.2f}".format(s)
            g = " {: <11}".format( w)  + " :  " + str(rsult)
            print( g )
            self. slp(t)

        breakdown.show(str(sm))
        return sm

def deg(rad):
    return rad/pi

def rad(deg):
    return pi * deg/180

def abc(astring):
    #take a string, put the 'words' in abc order...
    wd = astring.split(' ')
    rt = []
    for w in wd:
        rt.append( w , i)
    return rt #made this a string too tho.....


skl = 'CalTech CalSci CMU harveyMudd Berkley Cornell Stanford UC CSU Slo Po MIT Hop'
ivish = 'Stanford Harvard Mit Yale princeton Columbia Dude NotreDame Cornel Berkley USC UCLA'
vlginto = "Hi! My name is (rhymes with peachy) and I live in New York City. New videos on my channel every week! I upload vlogs, tech reviews, how-to / behind the scenes travel & lifestyle  "
prms = [ 1,  2,  3,  5,  7,  11,  17,  23,  37,  47,  57,  67,  79,  83,  91] #. . . ?
# iniit stuff here but whatever. . .
l = spit()
# l. slp(10)
a = l. tt(skl,  333,  21 )
a = l.adm(0)
print('   More schools... ')
# a = l. tt(ivish,  333,  51 )
print('   -- College acceptance test -- ')
# print( '   ', skl)
# print (a)
