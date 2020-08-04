'''
Created on Feb 13, 2016

@author: saul
'''
from ReadConfig import ReadConfig


class convert():

    val =  1600000
    '''

 # ====================== +++++++++++++++++++++
  # ====================== +++++++++++++++++++++
   # ====================== +++++++++++++++++++++
    working:  hours to month/year/day
    date ms to am/pm/ dwy

    //intermediate convertion strings not ready

    needs converting:
    why no ?  in python?  ^_-
    do this in c-+- ? ? ?
     # ====================== +++++++++++++++++++++
      # ====================== +++++++++++++++++++++
       # ====================== +++++++++++++++++++++
    private String secToString(long td){
        //format secs to display time nicely.
        long second = (td ) % 60
        long minute = (td / 60) % 60
        long hour = (td / ( 60 * 60)) % 24
        long day = (td / ( 60 * 60 * 24) )

        String m = (day > 0) ? day + "d" : ""
        m += (hour > 0) ? hour + "h" : ""
        m += (minute > 0) ? minute + "m" : ""
        m += String.format("%02ds", second)

        return m
    }
                print ("  " ,  "{:,.2f}".format( self.htoYears()) )
'''

    mparse = 0
    rc = 0

    def __init__(self, v=0):
        if v == 0: pass
        else:  self.val = v
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
        print ("Hours   :" , "{:,.1f}".format( self.getVal()) )
        print ("minutes : " , "{:,.1f}".format( self.hrtoMin()) )
        print ("seconds : " , "{:,.1f}".format( self.hrtoSec()) )
        print ("micros  : " , "{:,.2f}".format( self.hrtoMs()) )
        print ("nanos   : " , "{:,.0f}".format( self.hrtoNs()) )

 # split to switch on input operators h d w m y Me Cen Dec eon = 100kyr? 1m?
 # operation string fifo display
    def demoHr2yrs(self):
        print ("Hours " , "{:,.1f}".format( self.getVal()) )
        print ("Days " ,  "{:,.1f}".format(self.htoDays()) )
        print ("Weeks " , "{:,.1f}".format(self.htoWeeks()) )
        print ("Months " , "{:,.2f}".format( self.htoMonths()) )
        print ("Years " , "{:,.3f}".format( self.htoYears()) )
        print ("M " , "{:,.1f}".format( self.htoYears()//1000 ) )

    def demo(self):
        m = self
        if self.val > 10:
            m.demoHr2yrs()
            m.demoHr2ms()
        else:
            m.demoHr2ms()
            m.demoHr2yrs()


if __name__ == '__main__':
    # t = 20*7*52 #*1000
    # m = convert(t)
    # # m.setVal(t)
    # m.demo()
    # print( str(t) )
    rc = ReadConfig()
    args = rc. readInput("Enter a value(hours) to Convert:")
    t = args
    print("Value input: " + t)
    tt = int(t)
    m = convert(tt)
    m.demo()
    # m.testStrings(rc, "anything else?  ...")

    # m.getCommandArgs
