
import time
from math import pi, cos, sin, tan

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

        #spit words with delayed time to
        #read the stream because i ahte reading. . .
    def tt(self, msg,  tm,  t):
        ms = msg.split(' ')
        sm = 1
        for w in ms:
            print( w )
            self. slp(t)
            sm += t
        print(msg, end="\n")
        sm += tm*t*11
        return sm

def deg(rad):
    return rad/pi

def rad(deg):
    return pi * deg/180

hello = " ..."
vlginto = "Hi! My name is (rhymes with peachy) and I live in New York City. New videos on my channel every week! I upload vlogs, tech reviews, how-to / behind the scenes travel & lifestyle  "
prms = [ 1,  2,  3,  5,  7,  11,  17,  23,  37,  47,  57,  67,  79,  83,  91] #. . . ?
# iniit stuff here but whatever. . .
l = spit()
# l. slp(10)
a = l. tt(hello,  333,  11 )
print (a)
