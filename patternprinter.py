
import time
from math import pi, cos, sin, tan

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
        for i in range(0, c):
                if i % a == 0:
                    temp += bb
                else: temp += b
        print(temp)
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



l = pp()
l. tt(111888,  33,  "x",  '\n')
