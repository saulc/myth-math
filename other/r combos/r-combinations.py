
# Week 2 r-findCombinations
# group 13
# Saul Castro
# Huy Francis Nguyen

def openFile():
    file = open("test.txt", 'r')
    return file

def printFile(f):
    print(f.read())

def readInput():

    file = open("test.txt", 'r')
    s = str(file.read())
    words = s.split(" ");
    print(words)
    findCombinations(int(words[0]), int(words[1]) )

def findCombinations(r, n):
    print("R: " + str(r) + " n: " + str(n))
    combos = []
    for i in range(0, r):
        c = ""
        for j in range(1, n+1):
            # c += str(j)
            c += str(i)
            print("i: " + str(i) + " j: " + str(j))
        print("combo: " + c)
        combos.append(c)
    print(combos)

def permute(combos, l, r):

    if l == r:
        print (combos)
    else:
        for i in range(l, r + 1):
            combos = swap(combos, l, i)
            permute(combos, l + 1, r)
            combos = swap(combos, l, i)

def swap(combos, i, j):
    temp = combos[i]
    combos[i] = combos[j]
    combos[j] = temp
    return combos


def test():
    pass



if __name__ == '__main__':
    # config = openFile()
    # //f = printFile(config)
    # readInput()

    permute([1,2,3], 0, 2)
