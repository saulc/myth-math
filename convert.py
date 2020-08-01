'''
Created on Feb 13, 2016

@author: saul
'''




class convert():

    val =  1600000
    '''
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
'''
    def __init__(self, v):
        self.val = v

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

    def hrtoDay(self, td):
        day = (td / ( 60 * 60 * 24) )
        return day

    def secToDay(self, s):
        return self.hrtoDay(self.mintoHr(self.sectoMin(s)))

    def demo(self):
        print ("Hours " , "{:,.1f}".format( self.getVal()) )
        print ("Days " ,  "{:,.1f}".format(self.htoDays()) )
        print ("Weeks " , "{:,.1f}".format(self.htoWeeks()) )
        print ("Months " , "{:,.1f}".format( self.htoMonths()) )
        print ("Years " , "{:,.1f}".format( self.htoYears()) )
        print ("M " , "{:,.1f}".format( self.htoYears()//1000 ) )

if __name__ == '__main__':
    t = 20*7*52 #*1000
    m = convert(t)
    # m.setVal(t)
    m.demo()
    print( str(t) )
