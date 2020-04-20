'''
4/20/2020

@author: saul

some math based on the work - hour or "man-hour" - "man-month"
from 'The mythical man month'
'''
from convert import convert


class myth():

    conv = 0
    workers = 1000
    hoursper = 40 # 12*6
    amount = 1000000 #1 million base. 10x 1000x get interesting....
    hourly = 15  # lol more like 11....ish...

    def __init__(self):
        self.conv = convert()

    def getVal(self):
        return self.conv.getVal()
    def getWorker(self): return self.workers
    def setWorker(self, w): self.workers = w


    def demo(self):
        hrperyear = self.hoursper*52
        w = self.amount / (hrperyear*self.hourly)
        self.workers = int(w)
        self.conv.setVal(hrperyear*self.workers)
        print("$$$", "{:,}".format(self.amount ) )
        print("hours per:", self.hoursper)
        print('52 weeks / One year..')
        print(str(hrperyear) + " hours per year per worker")
        print('hourly $: ' , str(self.hourly) )
        print('annual $: ' , "{:,}".format(hrperyear*self.hourly) )

        print("Workers: " ,"{:,}".format( self.workers) )
        print('annual $: ' , "{:,}".format(self.hourly*self.conv.getVal() ) )
        print('Hours per year Total: ',"{:,}".format( self.conv.getVal()) )
        print("Converting for context...")
        self.conv.demo()

if __name__ == '__main__':
    m = myth()
    print ("Hours " , m.getVal())
    m.demo()
