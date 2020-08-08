'''
Created on 8720

@author: saul
'''


class bd():

    '''

 # ====================== +++++++++++++++++++++
  # ====================== +++++++++++++++++++++
   # ====================== +++++++++++++++++++++

    needs converting:
    why no ?  in python?  ^_-
    do this in c-+- ? ? ?
     # ====================== +++++++++++++++++++++


'''

    mparse = 0
    rc = 0
    val = 7.1

    def __init__(self, v=0):
        if v == 0: pass
        else:  self.val = v
        self. demo()
        # self.rc = ReadConfig("testing... 1 2 3")
        # self.mparse = self.rc.getCommandArgs(False)
        # print(self.mparse)
        # print(" read initial arguments done, if any.")


    def checkCommandArgs(self, inargs):
        print("Getting inital arguments .")
        v = inargs.getCommandArgs(True)
        print("returned args: " )
        print(v)
 # ====================== +++++++++++++++++++++
   # ====================== +++++++++++++++++++++
    def testStrings(self, inargs, msg):
        print(". . . --->AcMe rock.its<<---. . . ")
        print(" " + msg)
        v = inargs.readInput()
        print(v)
        self.checkCommandArgs(inargs)

 # ====================== +++++++++++++++++++++
   # ====================== +++++++++++++++++++++
    def getVal(self):
        return self.val

    def setVal(self, v):
        self.val = v

    def htoDays(self):
        return self.val / 24

    def htoMonths(self):
        return self.htoWeeks()/4

    def htoWeeks(self):
        return self.htoDays()/7

    def htoYears(self):
        return self.htoMonths()/12

    def mstoSec(self, ms): return ms//1000

    def sectoMin(self, s):
        second = (s ) % 60
        return  second

    def secto(self, s):
        minute = (s / 60) % 60
        return  minute

    def mintoHr(self, m):
        hour = (m / ( 60 * 60)) % 24
        return hour

    def hrtoDay(self):
        day = (self.val / ( 60 * 60 * 24) )
        return day

    def hrtoMin(self):
        min = (self.val  * 60  )
        return min

    def hrtoSec(self):
        min = (self.val  * 60 *60 )
        return min

    def hrtoMs(self):
        return 1000* self.hrtoSec()

    def hrtoNs(self):
        return 1000*1000* self.hrtoSec()
 # ====================== +++++++++++++++++++++
  # ====================== +++++++++++++++++++++
   # ====================== +++++++++++++++++++++


    def secToDay(self, s):
        return self.hrtoDay(self.mintoHr(self.sectoMin(s)))

    def demoHr2ms(self):
        print ('    ', "Hours   :" , "{:,.1f}".format( self.getVal()) )
        print ('    ', "micros  : " , "{:,.2f}".format( self.hrtoMs()) )
        print ('    ', "nanos   : " , "{:,.0f}".format( self.hrtoNs()) )

 # split to switch on input operators h d w m y Me Cen Dec eon = 100kyr? 1m?
 # operation string fifo display
    def demoHr2yrs(self):
        print ('    ', "Hours  : " , "{:,.1f}".format( self.getVal()) )
        print ('    ', "Days   : " ,  "{:,.1f}".format(self.htoDays()) )

    def demo(self):
        m = self
        if self.val > 10:
            m.demoHr2yrs()
            m.demoHr2ms()
        else:
            m.demoHr2ms()
            m.demoHr2yrs()

def getuserval(msg,  printInput=False ):
    print(msg)
    n = input()
    f = float( n )
    # i = int( n )
    if printInput:
        print("Value input: " ,    "{:.2f}".format( f )  )
    return


    #some blank functions/methods/what. . .
def t1( a):  print ('1    : ',  a)
def t1111(a):  print('1000 : ',  a)
 # ths = something conditional ?  ok :  no way;
 # condition, input,  tf,  ff
 # returned output
def qny(c,  arg,  f,  m):
    b = []
    if c :  b = f(arg)
    else :  b = m(arg)
    return b


if __name__ == '__main__':
    # t = 20*7*52 #*1000
        # prompt user for values,  do the math. with some formatting. .
        # t = getuserval("Enter a value( $ ) to analyze :",  True)
        # f = getuserval("Enter number of items (1. f):  ",  True)
        # # cv = convert()
        # m = bd(t)
        # m. setVal(f)
        #
        # m.demo()
        a = ' blah'
        aa = ['stuff',  'jumk',  'junk']
        print('?  test. . . ')
        t1(" blahhh")
        t1111(aa)
        qny( 0, aa, t1, t1111 )
