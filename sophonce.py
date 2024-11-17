import numpy as np
from numpy.polynomial import Polynomial
import math as math
import matplotlib.pyplot as plt
import random as rand
from time import time

from vectors import Vector


seed = 42
rand.seed(seed)

# STEPS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# abiogenesis
# time - 0.3
# eukaryogenesis
# time - 32 (formerly 2.027)
# differentiation
# complexity explosion
# CCE exaptions

steps_mn_bias  = [0.3,  2.203, 0.455, 0.606]
steps_sd_bias = [0.25, 0.827, 0.139, 0.27 ]

steps_mn_pure  = [0.3,  2.027, 0.44,  0.565, 0.531] 
steps_sd_pure = [0.25, 1.035, 0.149, 0.306, 0.01]

steps_mn = steps_mn_pure
steps_sd = steps_sd_pure

labels = ['Abiogenesis', 'Eukaryogenesis abs', 'Differentiation abs', 'Explosion abs', 'Biodiversity abs', 'Eukaryogenesis', 'Differentiation', 'Explosion', 'Biodiversity']
normals = [0,0,0,0,0]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def pinDown(mean, confidence, exp=0, integer=True) :
    rand.seed(seed+mean+confidence+exp)
    pinned = mean + rand.random()*confidence*2 - confidence
    pinned_exp = pinned * 10 ** exp
    if integer:
        return int(pinned_exp)
    else :
        return pinned_exp
    
eukar_adjust = 10**pinDown(math.log10(steps_mn_pure[1]) + 2.2, 0.5, 0, False)
steps_mn[1] = round(eukar_adjust,3)
print(eukar_adjust)

def norm(x, mn=0, sd=1):
    return (1 / (2 * np.pi * sd**2)**0.5) * (np.e ** (- (x - mn)**2 / (2 * sd**2)))



# ABSOLUTE STEP COMPLETION DISTRIBUTION
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def HardStepNormal(x, n):
    result = norm(x, steps_mn[n], steps_sd[n])
    #print(result)
    if result != 0:
        if math.log10(result) > -30 : return result
    return 0

def HardStepExp(x, n):
    result = np.e**(-(1/steps_mn[n])*x)
    if result != 0:
        if math.log10(result) > -30: return result
    return 0

def StepArray(step_func):
    xlist.append([step_func(i) for i in t])


def LogisticCurve(x,l,k,x0):
    return l / (1 + np.e**-(k * (x - x0)))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def Abiogenesis(x):
    #return HardStepNormal(x, 0) if x > 0.05 else 0
    return HardStepExp(x - 0.05, 0) if x > 0.05 else 0

def Eukaryogenesis(x):
    #return HardStepNormal(x, 1) if x > 0.1 else 0
    return HardStepExp(x, 1) if x > 0.1 else 0

def Differentiation(x):
    return HardStepNormal(x, 2) if x > 0.05 else 0

def Explosion(x):
    return HardStepNormal(x, 3) if x > 0.05 else 0

def CCE(x):
    return HardStepNormal(x, 4) if x > 0.05 else 0


def Biodiversity(x):
    l = 43.405
    k = 5
    x0 = 0.965425
    norm = 1.08320680813
    result = LogisticCurve(x, l, k, x0) / norm
    return result if x < 15 else l / norm


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

timespan = 100  # in Gyr
timestep = timespan/10000 # in Gyr
# if ratio above 10000, memory errory throws when making grid
t = [i*timestep for i in range(int(timespan/timestep))]

xlist = []

tstart = time()
def DistributeSteps():
    StepArray(Abiogenesis)
    StepArray(Eukaryogenesis)
    StepArray(Differentiation)
    StepArray(Explosion)
    #StepArray(CCE)
    StepArray(Biodiversity)

DistributeSteps()

tend = time()
print(tend - tstart, "\n")


# CHAINED STEP COMPLETION DISTRIBUTION
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

grid = []

def CombineArraytoGrid(array1, array2):
    a1 = np.asarray(array1)
    a2 = np.asarray(array2).reshape(len(array2),1)
    return a1 * a2

def CombineSteptoGrid(step1, step2, grid=grid):
    return CombineArraytoGrid(xlist[step1], xlist[step2])

def CombineStep(x, step1, step2, grid):

    result = 0
    xdec = int(x * 100)
    trunc_grid = grid[:xdec+1, :xdec+1]
    grid_diag = np.fliplr(trunc_grid).diagonal()
    result = np.sum(grid_diag)
    #for i in range(xdec):
        #j = i/100

        #result += grid[i][xdec - i]
    return result / 100

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ChainSteps():
    
    tstart = time()


    grid = CombineSteptoGrid(0,1)
    #print(grid)

    tend = time()
    print(tend - tstart)
    tstart = time()

    def Real_Eukaryo(x):
        #sumtstart = time()
        last = 0
        next = 1
        result = CombineStep(x, last, next, grid)
        #sumtend = time()
        #print(sumtend-sumtstart)
        return result

    xlist.append([Real_Eukaryo(i) for i in t])
    normal = sum(xlist[-1])
    xlist[-1] = [i/normal for i in xlist[-1]]


    tend = time()
    print(tend - tstart, "\n")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    tstart = time()

    grid = []
    grid = CombineSteptoGrid(5,2)
    #print(grid)

    tend = time()
    print(tend - tstart)
    tstart = time()

    def Real_Diff(x):
        last = 5
        next = 2
        return CombineStep(x, last, next, grid)

    xlist.append([Real_Diff(i) for i in t])
    #xlist.append([1 for i in t])
    normal = sum(xlist[-1])
    print(normal)
    xlist[-1] = [i * 1/normal for i in xlist[-1]]

    tend = time()
    print(tend - tstart, "\n")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    tstart = time()

    grid = []
    grid = CombineSteptoGrid(6,3)
    #print(grid)

    tend = time()
    print(tend - tstart)
    tstart = time()

    def Real_Expl(x):
        last = 6
        next = 3
        return CombineStep(x, last, next, grid)

    xlist.append([Real_Expl(i) for i in t])
    #xlist.append([1 for i in t])
    normal = sum(xlist[-1])
    print(normal)
    xlist[-1] = [i/normal for i in xlist[-1]]

    tend = time()
    print(tend - tstart, "\n")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    #tstart = time()

    #grid = []
    #grid = CombineSteptoGrid(7,4)
    ##print(grid)

    #tend = time()
    #print(tend - tstart)
    #tstart = time()

    #def Real_CCE(x):
    #    last = 7
    #    next = 4
    #    return CombineStep(x, last, next, grid)

    #xlist.append([Real_CCE(i) for i in t])
    ##xlist.append([1 for i in t])
    #normal = sum(xlist[-1])
    #xlist[-1] = [i/normal for i in xlist[-1]]

    #
    #tend = time()
    #print(tend - tstart)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    tstart = time()

    grid = []
    grid = CombineSteptoGrid(7,4)
    #print(grid)

    tend = time()
    print(tend - tstart)
    tstart = time()

    def Real_Biodiversity(x):
        last = 7
        next = 4
        return CombineStep(x, last, next, grid)

    xlist.append([Real_Biodiversity(i) for i in t])
    #xlist.append([1 for i in t])
    #normal = sum(xlist[-1])
    #xlist[-1] = [i/normal for i in xlist[-1]]

    
    tend = time()
    print(tend - tstart)

ChainSteps()

# GRAPH IT
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fig, ax = plt.subplots()
for i in range(len(xlist)):
    ax.plot(t, xlist[i], label=labels[i])
ax.legend()
plt.show()

# writing the text file
TL = open('sophonce' + str(timespan) + '.txt', "w")
TL.write('\n')
for i in range(1000):
    TL.write(str(xlist[-1][i]))
    TL.write(',')
