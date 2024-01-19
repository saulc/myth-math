'''
Created on 8/3/20

@author: saul

stats class to keep track of game values for each player
future version may be linked to a user item to hold stats for mutiple players

i don't like basebaall. . but i know most of the rules. . .

2 teams. 9 players each?
3 out, 3 in, 3 other. pitch, catch, short(mid)stop
time independent
1-4 offence vs. 3x3 defence
walks get runs. gdouble can get 2 runs?
basebaall is bs...
bounce counts!

'''


class myPair:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getName(self): return self.name

    def getValue(self): return self.value


class season:
    seasonAvgerage = 0
    seasons = [ ]

    def __init__(self,  avg,  seasonNum):
        self.seasonAvgerage = Avg
        self.seasons = (seasonNum,  avg)


''' ================================================

 +++++++++++++++++++++++++++++++++++++++++++++  '''
#
class pitch:
    # details for pitcher selection/ballpen. . .
    switch = False
    side = 1  # 0 switch 1 right 2 left
    style = 0

    name = 'one'
    speed = 101
    motion = 0
    curve = 0
    cx = 0
    cy = 0
    dv = 0
    vx = 0
    vy = 0

    vi = [0, 0, 0]
    vf = [0, 0, 0]
    spin = [0, 0, 0]
    zone = 5
    # a b c d e
    # p 1 2 3 f
    # o 4 5 6 g
    # n 7 8 9 h
    # m l k j i
    #

class pitcher:

    pitches = 0
    batters = 0
    strikes = 0
    swings = 0
    ball = 0
    bswings = 0
    foul = 0
    foultp = 0
    hit = 0
    bunt = 0


class hit:
    print("reading Input . . . ")
    # thisdict = {
    #   "brand": "Ford",
    #   "model": "Mustang",
    #   "year": 1964
    # } atbat++, on base(0123) 23,12,13,1, hit: single, double, tripple hr
    # bunt, update rbi. pitches, fouls...
    # update hitter avg...game vs season vs career counts
    
    thisHit = {
    'pitch' :  'blah' ,
    'game' :  'blah' ,
    'location' :  'blahblah' ,
    'misc' :  'blah'         }

    def printInfo(self):
        print(self.thisHit)


# at bat.
class hitting:
    seasonAvgerage = 0
    seasons = [ ]



    feildPos = 0
    # inf,  outf, pitch,  catch,  hit,  speed,
    # 123 678,  9,  545,
    atBat = 0
    strikes = 0
    ball = 0
    foul = 0
    foultp = 0
    pitches = 0
    hit = 0
    bunt = 0
    rbi = 0
    era = 0
    hitAvg = 0
    swingxx = 0
    stance = 0
    switch = False

    def __init__(self,  avg,  seasonNum):
        self.seasonAvgerage = Avg
        self.seasons = (seasonNum,  avg)


# skill, agressiveness, speed, # XX:
class feild:
    seasonAvgerage = 0
    seasons = [ ]

    def __init__(self,  avg,  seasonNum):
        self.seasonAvgerage = Avg
        self.seasons = (seasonNum,  avg)


        ''' ================================================

        +++++++++++++++++++++++++++++++++++++++++++++  '''


        ''' ================================================

        +++++++++++++++++++++++++++++++++++++++++++++  '''



class Stats:

    # black = pygame.Color(0, 0, 0)
    # white = pygame.Color(255, 255, 255)
    # green = pygame.Color(0,255,0)
    # blue = pygame.Color(0, 0,255)
    # red = pygame.Color(255,0, 0)
    # orange = pygame.Color(200,0, 100)
    #
    # colors = [red, orange, green, blue]

    dpower = 10

    def __init__(self,   score=1000, leagues=11):
        super().__init__()
        self.score = score
        self.shots = 0
        self.hits = 0
        self.gotHit = 0
        self.crash = 0
        self.powerUps = 0
        self.power = self.dpower
        self.seasons = 0
        self.leagues = leagues
        self.wZero = 1000  #main skill
        self.wOne = 100     #strength //major
        self.wTwo = 10      #weak   //minor
        self.ws = [ self.wZero, self.wOne, self.wTwo]

    def getStatsString(self):
        return 'Score: {0} | Seasons: {1} | Leagues: {2} | Shield: {3}'.format(self.score, self.seasons, self.leagues,  self.power)

    def getFullStats(self):
        items = []
        items.append( myPair('Game Stats', ''))
        items.append( myPair('Score', self.score) )
        items.append( myPair('Seasons', self.seasons) )
        items.append( myPair('Leagues', self.leagues) )
        items.append( myPair('Shield', self.power) )
        items.append( myPair('Shots', self.shots) )
        items.append( myPair('Hits', self.hits) )
        items.append( myPair('Been Hit', self.gotHit) )
        items.append( myPair('Crashes', self.crash) )
        items.append( myPair('Power Ups', self.powerUps) )

        # items.append( myPair('Main Weapon', 'Unlimited' ) )
        # items.append( myPair('Left Gun', self.wepons[1]) )
        # items.append( myPair('Right Gun', self.wepons[2]) )



        return items

    def setWepon(self, w, power):
        if w < len(self.wepons):
            self.wepons[w] = power
#         if w == 0: self.weponZero = power
#         elif w == 1: self.weponOne = power
#         elif w == 2: self.weponTwo = power

    def update(self):
        pass

    def reset(self):
        self.power = Stats.dpower


    def crashed(self, power):
        self.crash += 1
        self.power -= power

    def hit(self):
        self.score += 10
        self.hits += 1

    def misses(self):
        return self.shots - self.hits

    def powerup(self, pup):
        self.power += pup.power
        for i in range(len(self.wepons)):
            self.wepons[i] += pup.wepons[i]

        self.powerUps += 1
        self.score += 100


    def levelUp(self):
        self.level += 11
        self.score += 10000

    def getScore(self):
        return self.score



if __name__ == '__main__':
    h = hit()
    h.printInfo()

    s = Stats(score = 100, leagues=2 )
    s.hit()
    s.hit()
    print(s.getStatsString())
    for l in s.getFullStats():
        print(l.getName() + " : " + str(l.getValue() ))
