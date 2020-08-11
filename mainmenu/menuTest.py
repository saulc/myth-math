
'''
    manager tools for scheduling. time shifts/blocks

    81020 saulc
'''

import ager
import breakup

class menut:
    op = ['Main menu', 'View Tasks', 'View Worker Info', 'aux', 'idk', 'Some', ' thing']
    lastPick = 1
    mem  = 0
    numoptions = 4
    name = ' Acme test menu '

    def __init__(self, noptions=5):
        self.numoptions = noptions
        if noptions > len( self.op ): self.numoptions = len(self.op)
        # self.showMenu(True)
        breakup.show(' Acme menu running... ')


    def showMenu(self,   printerOn=False):
        gg = self.getMenuInfo( )
        if printerOn: breakup.show(gg)
        return True ##add a break maybe...


    def getMenuInfo(self,   printerOn=False):
        gg = [ ]
        gg.append(self.op[0])
        for i in range(1,self.numoptions):
            # if i == self.lastPick: mg += ' ~'
            mg = str(i) +' ' + self.op[i]
            gg.append(mg)
        if printerOn: breakup.show(gg)
        return gg

    #idk probably useful later on...
    def pickOp(self, i):
        if i > self.numoptions: i %= self.numoptions
        self.mem = self.lastPick
        self.lastPick = i
        return self.mem

    def navto(self, a, b):
        mg = ' navigating from ', str(a), ' --> ', str(b)
        breakup.show(mg)

# show a msg and get a response, expect a float/int...
def getuserval(msg,  printInput=False ):
    print(msg)
    n = input()
    f = 1
    if msg == '' or msg == ' ': f = 4
    try:
        f = int(n)
        mg = 'Option entered: ' + n
        breakup.show(mg)
    except ValueError:
        # Handle the exception
        print('err. Please enter an integer')
    # i = int( n )
    if printInput:
        f = float( n )
        print("Value input: " ,    "{:.2f}".format( f )  )
    return f

if __name__ == '__main__':
#for testing/ examples only
    br = True
    mmu = menut(5)
    while br :
        br = mmu.showMenu(True)
        up = getuserval('Pick an Option.')
        frm = mmu.pickOp(int(up))
        mmu.navto(frm, up) #...
