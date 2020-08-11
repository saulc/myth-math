'''
Created on 8920

@author: saul
'''


class bd():

    '''
    # a starting point for break/build
    need some context to clean this up. .
    a drop would probably help. . . .

    basic req:
        .  oop. object no tuples
        .  build up from item cost/value
        .  clean variable names
        .  cost * items = # REV
        .  matc + wk + leaks = opcost
        rev - opcost = profit/loss (-+) red/black trees? bst...
        profit breakdown ==> stockbuybackbs or bonus?
        . . . . . . .
        fu math should've done this on the beach. . . .
        what if the noobs were preprogrammed for connectivity?
 # ====================== +++++++++++++++++++++
'''


    val = 1.1
    div = 1

    def __init__(self, v=0):
        if v == 0: pass
        else:  self.val = v
 # ====================== +++++++++++++++++++++
   # ====================== +++++++++++++++++++++
    def testStrings(self, inargs, msg):
        print(". . . --->AcMe rock.its<<---. . . ")
        print(" " + msg)
        v = inargs.readInput()
        print(v)
        self.checkCommandArgs(inargs)

 # ====================== +++++++++++++++++++++

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

def show(msgs, pre = '   ', sux = '    . . . '):
    #chekc if its a string or list of strings...
    #send them to show to display std pre/suf
    if isinstance(msgs, list):
        # print('  -- list found ---')
        for m in msgs:
            shows(m, pre, sux)
    elif isinstance(msgs, str):
        # print('  -- str found ---')
        shows(msgs, pre, sux)  #expects strings, so i'm not checking others now...
    else : print('  -- invalid input found ---')

#add pre/suf to string then print..
def shows(msg,pre, sux):
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

def showDemo(t = 10000):

    # t = 27777
    f = 15
    tt=0
    l = [t, f, tt]
    # print('-- acme rockets made in rrlabs -_^')
    show('mepmep!!!')
    # tt = showDiv(t, f , True)
    show('Even split in ' + str(f) + ' parts. ')
    # l[2] +=
    evenSplit(t, f, True, True)
    show('3/3 split in ' + str(f) + ' parts. ')
    l[2] += bigSplit(t, f, 3, True)
    total = l[2]
    # rk = rankSplit(t, 3, True)
    show( " total $ {:,.2f}".format( total)  )
    show( " split $ {:,.2f}".format( t )  )
    show('  --> Break Down {:,.2f}'.format(f) +' parts. done.')
    return total


if __name__ == '__main__':
        # prompt user for values,  do the math. with some formatting. .
        t = getuserval("Enter a value( $ ) to analyze :",  True)
        # f = getuserval("Enter number of items (1. f):  ",  False)
        tl = showDemo(t)
        show( "xx $ {:,.2f}".format(tl ) )
