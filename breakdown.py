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


    val = 1.1
    div = 1

    def __init__(self, v=0):
        if v == 0: pass
        else:  self.val = v
        # self. demo()
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

    def getDivs(self):
        return self.val

    def setDivs(self, v):
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
        qny( True, ['demo'], self.demoHr2yrs(), self.demoHr2ms() )


# -------------------------------------------------------------

    #some blank functions/methods/what. . .
def t11(): print('non') #print('no initial args')
def t1( a):  print ('1    : ',  a)
def t1111(a):  print('1000 : ',  a)
 # ths = something conditional ?  ok :  no way;
 # condition, input,  tf,  ff
 # returned output
def qny(c,  arg,  f,  m):
    b = []
    # el
    if len(arg) == 0: #t11()
        if c :  b = f()
        else :  b = m()
    # elif len(arg) == 1:
    #         if c :  b = f(arg)
    #         else :  b = m(arg)
    return b

def qtest():
    #manage arguments for gen funcs.
    aaa = []
    a = ' blah'
    aa = ['stuff',  'jumk',  'junk']
    print('?  test. . . ')
    t1(" blahhh")
    t1111(aa)
    for i in range(11):
        if i%3==1: aa.append(a)
        qny( i%4==0, aaa, t1, t11 )


# -------------------------------------------------------------
#
#  "{:><15}|{:-^10}|{:<>15}".format(left_aligned, center, right_aligned)
# 'Left Align>>>>>|-Centered-|<<<<Right Align'

def evenSplit(a, n, showSplit=False, si = False):
    s = a // n # NOTE: whole percentage only. no change ;p
    r = a % n
    st = '{:,.2f}'.format(n) + ' split : {:,.2f}'.format(a) + ' ; extra: {:,.2f}'.format(r)
    if showSplit:
        show(st)
        for i in range(0, int(n) ):
            show( "{: <11}".format(i+1 ) + "...  $:  {:,.2f}".format(s)  )
    if si: show(" n:  {: <3}".format(n) + "   x p: {:,.2f}".format(s) +"  extra:  {:,.2f} ".format(r) )
    return s

def bigSplit(a, n, nn, showSplit=False):
    hf = a/3
    evenSplit(hf, n, showSplit)
    evenSplit(hf, nn, showSplit)
    return hf

def adsp(msg):
    msg+= '\n'
    return msg

def showDiv( amount=10000.00, divs=11.1, sh=False):
    # self.setVal(amount)
    # self.setDivs( divs)
    # show('  --> Break Down in to ' + str( divs ) + ' parts, ')
    # show('    inital   : {:,.2f}'.format( amount ) )
    p, e = evenSplit(amount, divs, sh)

    msg = 'Even split Parts: {:,.2f}'.format( divs )
    show(msg)
    msg = ''
    msg += '    ex: {:,.2f}'.format(e)
    msg += '    x: {:,.2f}'.format( p )
    msg = adsp(msg)
    msg += '   3 way split / x even split'
    show( msg )


    if divs >= 5.0:
        total = e + bigSplit(amount, 3, divs-3, sh)
    else :
        total = e + bigSplit(amount, 3, 3, sh)
    if sh: show(' own {:,.2f}'.format(divs) )
    # show(' gettin it...')
    show('  --> Break Down {:,.2f}'.format(divs) +' parts. done.')
    return total
# -------------------------------------------------------------

def rankSplit(a, n, showSplit=False, si = False):
    nn = n+2    #one part to split
    s = a// nn
    ss = s/n #i dont not not not not know if if know what i'm doing here, maybe...
    r = a%nn + s #one part for extra
    st = '{:,.2f}'.format(n) + ' split : {:,.2f}'.format(a) + ' ; extra: {:,.2f}'.format(r)
    if showSplit:
        show(st)
        for i in range(0, int(n) ):
            show( " {: <5}".format(i+1 ) + "...  $:  {:,.2f}".format(s+(n-i)*ss)  )
    if si: show(" n:  {:.0f}".format(n) + "   x p:  {:,.2f}".format(s) +" extra:  {:,.2f}".format(r) )
    return r


# -------------------------------------------------------------

def show(msg, pre = '   ', sux = '    . . . '):
    s = pre + str(msg)
    l = len(s)
    y = 55-len(sux)-l
    for i in range(y): s+= ' '
    s += sux
    print(s)
    return s

# show a msg and get a response, expect a float/int...
def getuserval(msg,  printInput=False ):
    print(msg)
    n = input()
    f = float( n )
    # i = int( n )
    if printInput:
        print("Value input: " ,    "{:.2f}".format( f )  )
    return f
def toc(a):
    return a *9876

def showL(lst, showIndex = False):
    i = 0
    for e in lst:
        f = float(e)
        i+=1
        show( '{:.0f}'.format(i) + '  {:.2f}'.format(f))
# -------------------------------------------------------------

if __name__ == '__main__':
    # t = 20*7*52 #*1000
        # prompt user for values,  do the math. with some formatting. .
        # t = getuserval("Enter a value( $ ) to analyze :",  True)
        # f = getuserval("Enter number of items (1. f):  ",  False)
        t = 11*365*10   #*1000000
        f = 15
        tt=0
        l = [t, f, tt]
        # showL(l)
        # cv = convert()
        # m = bd(t)
        # m. setVal(f)
        # print('-- acme rockets made in rrlabs -_^')
        show('mepmep!!!')
        tt = showDiv(t, f , True)
        rk = rankSplit(t, 3, True)
        show( " total $ {:,.2f}".format( tt)  )
