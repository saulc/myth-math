'''
Created on Feb 13, 2016

@author: saul
'''




class convert():

    val = 1600000

    def __init__(self):
        pass

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
    def demo(self):
        print ("Hours " , "{:,.1f}".format( self.getVal()) )
        print ("Days " ,  "{:,.1f}".format(self.htoDays()) )
        print ("Weeks " , "{:,.1f}".format(self.htoWeeks()) )
        print ("Months " , "{:,.1f}".format( self.htoMonths()) )
        print ("Years " , "{:,.1f}".format( self.htoYears()) )

if __name__ == '__main__':
    m = convert()
    m.demo()
