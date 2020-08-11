
import time
from math import pi, cos, sin, tan
import breakdown
#test program to visulaize led sequences.

class pp:
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
    def idk(self, c, a=44, b="-",  bb ="\n"):
        self. num = c
        temp = ''
        lns = 0
        rm =  (a*lns)
        bk =  c//a // 5
        for i in range(0, c):
                if i % a == 0 or lns % 5 == 0:
                    temp += bb
                    lns += 1

                else: temp += str(i).zfill(4) + ' '

        print(str(c) ,  ' chars x ',  str(a),  ' cols   xx',  str( bk ))
        print(lns,  ' lines x ',  str(a),  ' cols  tl: ',  str(rm))
        # breakdown. show(temp)
        return temp


    def tt(self, c, a=44, b="-",  bb =" "):
        self. num = c
        temp = ''
        for i in range(0, c):
                if i % a == 0:
                    temp += bb
                else: temp += b
        print(temp)
        return temp

def deg(rad):
    return rad/pi

def rad(deg):
    return pi * deg/180

# fuck you time. ^_^
leap = 365*4+1
y = leap // 100
y = 20
m = y /8
lm = " {: <5}".format( leap ) + " {: <15}".format( y ) + " {: <25}".format( m )
breakdown. show('# fuck you time!.   ^_^')
breakdown. show(lm)
l = pp()
onehundayz =int( leap//3.14159 )
grd = l. idk(llp,  y)
# breakdown. show(grd)
