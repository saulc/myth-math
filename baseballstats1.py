'''
Created on 8/3/20

@author: saul

stats class to keep track of game values for each player
future version may be linked to a user item to hold stats for mutiple players

i don't like basebaall. . .


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
    switch = false
    side = right
    style = non

    name = 'one'
    speed = 99
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
    rib = 0
    era = 0
    hitAvg = 0
    swingxx = 0
    stance = 0
    switch = false





    def __init__(self,  avg,  seasonNum):
        self.seasonAvgerage = Avg
        self.seasons = (seasonNum,  avg)

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



class Stats(Item):

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    green = pygame.Color(0,255,0)
    blue = pygame.Color(0, 0,255)
    red = pygame.Color(255,0, 0)
    orange = pygame.Color(200,0, 100)

    colors = [red, orange, green, blue]

    dpower = 10

    def __init__(self, swidth, sheight, score=1000, leagues=11):
        super().__init__(0, 0)
        self.height = sheight
        self.width = swidth
        self.score = score
        self.shots = 0
        self.hits = 0
        self.gotHit = 0
        self.crash = 0
        self.powerUps = 0
        self.power = power
        self.Seasons = level
        self.Leagues = leagues
        self.wZero = 1000  #main skill
        self.wOne = 100     #strength //major
        self.wTwo = 10      #weak   //minor
        self.ws = [ self.wZero, self.wOne, self.wTwo]

    def getStatsString(self):
        return 'Score: {0} | Seasons: {1} | Leagues: {2} | Shield: {3}'.format(self.score, self.lives, self.level, self.power)

    def getFullStats(self):
        items = []
        items.append( myPair('Game Stats', ''))
        items.append( myPair('Score', self.score) )
        items.append( myPair('Seasons', self.level) )
        items.append( myPair('Leagues', self.leagues) )
        items.append( myPair('Shield', self.power) )
        items.append( myPair('Shots', self.shots) )
        items.append( myPair('Hits', self.hits) )
        items.append( myPair('Been Hit', self.gotHit) )
        items.append( myPair('Crashes', self.crash) )
        items.append( myPair('Power Ups', self.powerUps) )

        items.append( myPair('Main Weapon', 'Unlimited' ) )
        items.append( myPair('Left Gun', self.wepons[1]) )
        items.append( myPair('Right Gun', self.wepons[2]) )



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
