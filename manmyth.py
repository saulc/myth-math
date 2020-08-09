'''
4/20/2020

@author: saul

some math based on the work - hour or "man-hour" - "man-month"
from 'The mythical man month'
'''
from convert import convert

from ReadConfig import ReadConfig
import breakdown

class myth():

    conv = 7250
    workers = 10*1000000
    hoursper =  33 #40 # 12*6
    amount =  1000*1000
    # amount = 277031758 # *10000000*1000
    # amount = 277031758 # *10000000*1000
    # 200 quadrillion = 15m x 12.82 billion global basic income?
    # us/ 15k x 320m. 4t per year...
    #us gdp 2020-1 = 20 trillion.
    #1mill x 1mill = 1 trillion.
    #1 million base. 10x 1000x get interesting....
    hourly =  111 #11  # lol more like 11....ish...
    yearx = 1

    def __init__(self,  cv=0):
        if cv == 0:  self. amount = 1000*1000
        else:  self. amount = cv
        self.conv = convert(self.conv)

    def setVal(self, v):
        return self.conv.setVal(v)

    def getVal(self):
        return self.conv.getVal()
        ## number of workers for set amount of time/amount
    def getWorker(self): return self.workers
    def setWorker(self, w): self.workers = w
    def getHrRate(self): return self.hourly
    def setHrRate(self, w): self.hourly = w

    def setYears(self,  y):  self. yearx = y

    def compountInterest(self,  p, r,  n, t):
        p = (1 + r/n)^nt
        return p
    ## TODO: recursion refresh
    # find/redo fractional/decimal calc. add fractional powers/exp
    def exponets(self, b, a):
            tt = 2
            tm = 0
            for i in range(a):
                msg = str(i+1) + ": b^n ~~ " + str(tt)
                tt *= b
                tm += tt*105
                print( str(i+1)+ ' p ' , "{:,}".format( tt) , "{:,}".format( tm), "{:,}".format( tm-tt) )


    def demo(self):
        hrperyear = self.hoursper*52
        yrhr = 24*7*52
        offhr = yrhr - hrperyear
        w = self.amount / (hrperyear*self.hourly)
        self.workers = int(w)
        self.conv.setVal(hrperyear*self.workers)
        an = hrperyear*self.hourly
        tl = hrperyear*self.hourly * self. yearx

        print(' {    ')
        print('   {  ')
        print( '     ',  "$$$", "{:,}".format(self.amount ) )
        print('     ',  "hours per week:", self.hoursper)
        print('     ',  '52 weeks / One year..')
        print('     ',  str(hrperyear) + " hours per year per worker")
        print('     ',  str(offhr) + " hours off")
        print('     ',  str(yrhr) + " hours-> year")
        print('     ',    "  {:.2f}".format(100*hrperyear/yrhr), "% time working billed. "  )
        print('     ',  'annual $: ' , "{:,}".format( an ) )
        print('     ',  'month $: ' , "{:,}".format(self.hoursper * self.hourly * 4) )
        print('     ',  'weekly $: ' , "{:,}".format(self.hoursper * self.hourly) )
        print('     ',  'hourly $: ' , str(self.hourly) )
        print('  }  ')

        print('     ',  'years #: ' , "{:,}".format(self. yearx) )
        print('     ',  'Total $: ' , "{:,}".format( tl ) )
        print('     ',  '___')
        print('     ',  "units: " ,"{:,}".format( self.workers) )
        print('     ',  'annual $: ' , "{:,}".format(self.hourly*self.conv.getVal() ) )
        print('     ',  'rem $: ' , "{:,}".format(self.amount - hrperyear*self.hourly*self.workers) )
        print('     ',  'rem $: ' , "{:.2f}".format(self.amount - hrperyear*self.hourly*self.workers) )
        print('     ',  'Hours per year Total: ', "{:,}".format( self.conv.getVal()) )
        print('     ', 'note : ',  "Converting for context...")
        print('     ')
        self.conv.demo()
        # print('     ',  "Years: ", "{:,.2f}".format( self.conv.htoYears() ) )
        # print('  . . .  ')
        return an,  tl

    def d2(self):

            print("----")
            print( str(100*24))
            # print("----")
            # aa = 7000
            # bb = 34359738368
            # c = bb/aa
            # print("..." , str( aa) )
            # print("..." , str( bb) )
            # print("..." , str( c) )
            # cv = convert(aa)
            # cv.demo()
            # print("----")
            m = myth()
            print ("Hours " , m.getVal())
            # m.demo()
            m.exponets(2, 22)
            m.exponets(3, 22)

def getuserval(msg,  printInput=False ):
    print(msg)
    n = input()
    i = int( n )
    if printInput:
        print("Value input: " ,  "{:.2f}".format( i) )
    return i


if __name__ == '__main__':

    # c = 5
    # print("..." , str( c) )
    # cv = convert(c)
    # # cv.setVal()
    # cv.demo()
    # print("----")

    # m = myth()
    # m.demo()
    # 1 year == 8760 == 525600

    tt =      67773311
    hrt = 752 #34359738368
    years = 1
    # prompt user for values,  do the math. with some formatting. .
    # t = getuserval("Enter a value( $ ) to analyze time divisions:",  True)
    # hrt = getuserval("Enter a hourly rate( $/hr ) : ")
    # years = getuserval("Enter #yx:  ",  True)
    # cv = convert()
    m = myth(tt)
    m. setHrRate(hrt)
    m. setYears(years)
    y,  t = m.demo()
    msg = 'Starting Value $ {:.2f}'.format(y) + ' total $: {:,.2f}'.format(t)
    breakdown.show(msg)
    div = 12 + 3 + .3 #mrent , save,spend, tax, kids?/invent?/hobbies...
    # rn = breakdown.showDiv( t ,div) #, True)
    # msg = 'returned Value $ {:.2f}'.format(rn) + ' \n'
    # breakdown.show(msg)

    er = breakdown.rankSplit( tt , 11, True, True)
    for i in range(3,14):
        ee = breakdown.evenSplit( er , i, False, True)
    # rn = breakdown.bigSplit( t ,3, div, True)
        msg = 'returned Value $ {:,.2f}'.format(ee) + ' \n'
    breakdown.show(msg)




    # cv.printTime()
