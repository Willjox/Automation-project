import collections
import random
import time
import math
def stddev(results, average):
    y= []
    for x in results:
        y.append((x - average)**2)
    return math.sqrt( ( (sum(y))/z) )


def switchBack(conveyor):
    a = conveyor.pop()
    b = conveyor.pop()
    conveyor.appendleft(b)
    conveyor.appendleft(a)
    return conveyor

def switchFront(conveyor):
        a = conveyor.pop()
        b = conveyor.pop()
        conveyor.append(a)
        conveyor.append(b)
        return conveyor
def moveBack(conveyor):
    a = conveyor.pop()
    b = conveyor.pop()
    conveyor.appendleft(a)
    conveyor.appendleft(b)
    return conveyor

def xToBack(i , conveyor):
    x = conveyor[-i]
    conveyor.remove(x)
    conveyor.appendleft(x)
    return conveyor


def setupConveyor():
    nbr = [1 , 2 , 3 , 4 , 5]
    conveyor = collections.deque([])
    while len(nbr) != 0:
        conveyor.append(nbr.pop(random.randint(0, len(nbr) - 1 ) ) )
    #print(conveyor)
    return conveyor

def checkOrder(conveyor):
    #print(list(conveyor),"\r",end="")
    #time.sleep(0.1)
    if list(conveyor) == [5 , 4 , 3 , 2 , 1]:
        return True
    else:
        return False

def bubbleSort(conveyor):
    iterations = 0
    while not checkOrder(conveyor):
        if (conveyor[-1] == 5 )& (conveyor[0] == 4):
            conveyor = xToBack(1 , conveyor)
        elif conveyor[-2] < conveyor[-1]:
            conveyor = xToBack(2, conveyor)
        else:
            conveyor = xToBack(1, conveyor)
        iterations += 1
    print("")
    return iterations


#def alg1(conveyor):
z = 100
i = 0
results = []
while i<z:
    results.append(bubbleSort(setupConveyor()))
    i+=1
avg = sum(results)/len(results)
s = stddev(results,avg)
ci = 2*3.66*s/(math.sqrt(z))
print("bubbleSort avrage iterations: ", avg)
print(ci)
