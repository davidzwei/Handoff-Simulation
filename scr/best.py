import matplotlib.pyplot as plt 
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import random
import math
from numba import jit
import statistics

class car:
    def __init__(self, initx, inity, initdir, initserviceB, initserviceT, initserviceE, initserviceO):
        self.x = initx
        self.y = inity
        self.direction = initdir  #top: 0, right: 1, bottom: 2, left: 3
        self.serviceB = initserviceB  #topleft: 0, topright: 1, botleft: 2, botright: 3
        self.serviceT = initserviceT
        self.serviceE = initserviceE
        self.serviceO = initserviceO


x = 1 - math.exp(-0.5)  #1/2, 0.39
y = 1 - math.exp(-1/3)  #1/3, 0.28
z = 1 - math.exp(-0.2)  #1/5, 0.18

speed = 10      #(m/s)
pmin = 10
#p = 0.03224053668
e = 5
t = 15
station = [(360,680), (660,658), (330,350), (640,310)]
totalpowerB = 0
handOffBest = 0

def changedirection(car, orig):
    if(car.x % 1000 == 0 and car.y % 1000 == 0) : 
        if(car.x == 0 and car.y == 0): #左下
            if (orig == 2):
                orig = 1
            elif (orig == 3):
                orig = 0
        elif (car.x == 1000 and car.y == 0): #右上
            if (orig == 1):
                orig = 2
            elif (orig == 0):
                orig = 3
        elif (car.x == 0 and car.y == 1000): #左上
            if(orig == 0):
                orig = 1
            elif(orig == 3):
                orig = 2
        elif (car.x == 1000 and car.y == 1000): #右下
            if (orig == 2):
                orig = 3
            elif (orig == 1):
                orig = 0         
    else:
        randnum = random.randrange(5) + 1
        if(randnum == 1): #turn left , 1/5
            orig = orig - 1 
        elif(randnum == 2): #turn right, 1/5
            orig = orig + 1

        if(orig == -1): #左
            orig = 3
        orig = orig % 4
        car.direction = orig


def goDirection(car, direction):
    if(direction == 0):
        car.y += speed
    elif(direction == 1):
        car.x += speed
    elif(direction == 2):
        car.y -= speed
    elif(direction == 3):
        car.x -= speed

def go(car):
    if(car.x % 100 == 0 and car.y % 100 == 0):
        changedirection(car, car.direction)
    goDirection(car, car.direction)


#enter
def carEnter(cars):
    for j in range(36):
        enter = random.random() < z
        if(j == 0): #from top left to clockwise top
            if(enter):
                cars.append(car(100, 0, 2, 0, 0, 0, 0))
        elif (j == 1):
            if (enter):
                cars.append(car(200, 0, 2, 0, 0, 0, 0))
        elif (j == 2):
            if (enter):
                cars.append(car(300, 0, 2, 0, 0, 0, 0))
        elif (j == 3):
            if (enter):
                cars.append(car(400, 0, 2, 0, 0, 0, 0))
        elif (j == 4):
            if (enter):
                cars.append(car(500, 0, 2, 0, 0, 0, 0))
        elif (j == 5):
            if (enter):
                cars.append(car(600, 0, 2, 1, 1, 1, 1))
        elif (j == 6):
            if (enter):
                cars.append(car(700, 0, 2, 1, 1, 1, 1))
        elif (j == 7):
            if (enter):
                cars.append(car(800, 0, 2, 1, 1, 1, 1))
        elif (j == 8):
            if (enter):
                cars.append(car(900, 0, 2, 1, 1, 1, 1))
        elif (j == 9):#right
            if (enter):
                cars.append(car(1000, 900, 3, 1, 1, 1, 1))
        elif (j == 10):
            if (enter):
                cars.append(car(1000, 800, 3, 1, 1, 1, 1))
        elif (j == 11):
            if (enter):
                cars.append(car(1000, 700, 3, 1, 1, 1, 1))
        elif (j == 12):
            if (enter):
                cars.append(car(1000, 600, 3, 1, 1, 1, 1))
        elif (j == 13):
            if (enter):
                cars.append(car(1000, 500, 3, 1, 1, 1, 1))
        elif (j == 14):
            if (enter):
                cars.append(car(1000, 400, 3, 3, 3, 3, 3))
        elif (j == 15):
            if (enter):
                cars.append(car(1000, 300, 3, 3, 3, 3, 3))
        elif (j == 16):
            if (enter):
                cars.append(car(1000, 200, 3, 3, 3, 3, 3))
        elif (j == 17):
            if (enter):
                cars.append(car(1000, 100, 3, 3, 3, 3, 3))
        elif (j == 18): #down
            if (enter):
                cars.append(car(900, 0, 0, 3, 3, 3, 3))
        elif (j == 19):
            if (enter):
                cars.append(car(800, 0, 0, 3, 3, 3, 3))
        elif (j == 20):
            if (enter):
                cars.append(car(700, 0, 0, 3, 3, 3, 3))
        elif (j == 21):
            if (enter):
                cars.append(car(600, 0, 0, 3, 3, 3, 3))
        elif (j == 22):
            if (enter):
                cars.append(car(500, 0, 0, 3, 3, 3, 3))
        elif (j == 23):
            if (enter):
                cars.append(car(400, 0, 0, 2, 2, 2, 2))
        elif (j == 24):
            if (enter):
                cars.append(car(300, 0, 0, 2, 2, 2, 2))
        elif (j == 25):
            if (enter):
                cars.append(car(200, 0, 0, 2, 2, 2, 2))
        elif (j == 26):
            if (enter):
                cars.append(car(100, 0, 0, 2, 2, 2, 2))
        elif (j == 27): # left
            if (enter):
                cars.append(car(0, 100, 1, 2, 2, 2, 2))
        elif (j == 28):
            if (enter):
                cars.append(car(0, 200, 1, 2, 2, 2, 2))
        elif (j == 29):
            if (enter):
                cars.append(car(0, 300, 1, 2, 2, 2, 2))
        elif (j == 30):
            if (enter):
                cars.append(car(0, 400, 1, 2, 2, 2, 2))
        elif (j == 31):
            if (enter):
                cars.append(car(0, 500, 1, 2, 2, 2, 2))
        elif (j == 32):
            if (enter):
                cars.append(car(0, 600, 1, 0, 0, 0, 0))
        elif (j == 33):
            if (enter):
                cars.append(car(0, 700, 1, 0, 0, 0, 0))
        elif (j == 34):
            if (enter):
                cars.append(car(0, 800, 1, 0, 0, 0, 0))
        elif (j == 35):
            if (enter):
                cars.append(car(0, 900, 1, 0, 0, 0, 0))
        

def power(car, station):
    xdiff = abs(car.x - station[0])
    ydiff = abs(car.y - station[1])
    dist = (xdiff ** 2 + ydiff ** 2) ** (1/2)  #d = (x^2 + y^2)^(1/2)
    if(dist == 0):
        return 100
    else:
        return 67 - 20 * math.log(dist, 10) #修正


def checkHandoff(car):
    global handOffBest
    global totalpowerB
    global handoff

    powerRec = []
    powerRec.append(power(car, station[0]))
    powerRec.append(power(car, station[1]))
    powerRec.append(power(car, station[2]))
    powerRec.append(power(car, station[3]))
    pnew = max(powerRec)
    newservice = powerRec.index(max(powerRec))
    poldB = power(car, station[car.serviceB])
    
    if(pnew > poldB): #best
        totalpowerB += pnew
        car.serviceB = newservice
        handOffBest += 1
    else:
        totalpowerB += poldB
    

#init
carToRemove = []
cars = []
handOffPlotBest = []
carnum = 0
handOff = []

#simulation starting here 86400s
for i in range(86400): 
    print(i)
    carToRemove.clear()
    carEnter(cars)
    for drivingCar in cars:
        if (drivingCar.x < 0 or drivingCar.x > 1000 or drivingCar.y < 0 or drivingCar.y > 1000):
            carToRemove.append(drivingCar) #leave
        else:
            checkHandoff(drivingCar)
            go(drivingCar)
    for toremove in carToRemove:
        cars.remove(toremove)
    handOffPlotBest.append(handOffBest)
    if(i<=0):
        handOff.append(handOffBest)
    else:
        x = handOffPlotBest[-1] - handOffPlotBest[-2]
        handOff.append(x)
    carnum += len(cars)
    #print('cars: ', len(cars))


print(len(cars))
print("best: ", handOffBest, "handoffs")
print('avgPowerBest', totalpowerB / carnum)
print()

print("avg handoff: ", handOffPlotBest[-1]/86400)
#avgPow = ((totalpowerM / carnum)+(totalpowerB / carnum))/2
print(sum(handOff))

fig = plt.figure(1, figsize=(18, 7))
gs = gridspec.GridSpec(1, 2, width_ratios=[3, 2])
plt.subplot(gs[0])
plt.plot(handOff, label='Best', linewidth=1, alpha=0.7)
plt.title('Handoffs of Best Policies with lambda = 1/5')
plt.xlabel('Second')
plt.ylabel('Handoffs')
plt.legend()


plt.subplot(gs[1])
plt.text(0, 0.8, 'lumbda: 1/5 ', fontsize=18)
plt.text(0, 0.6, 'Handoffs of Best Policy: {:.3f} times'.format(handOffBest), fontsize=18)
plt.text(0, 0.4, 'Average Power of Best Policy: {:.3f} dBm'.format(totalpowerB / carnum), fontsize=18)

plt.axis('off')


plt.savefig('best.png')
plt.show()


