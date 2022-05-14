import random
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from math import ceil

def Bernoulli_discription(p):
    u = random.random()
    if u <= p:
        r = 1
    else:
        r = 0
    return r

def PMF(p,n,t):
    q = 1-p
    y=[]
    for i in range(n):
        if t[i]==0:
            y.append(q)
        else:
            y.append(p)
    return y

def sampaling (N,p,t):
    sampl=[]
    for i in range(t):
        sampl.append(0)
    for i in range(len(sampl)):
        sampl[i] = []
    # print(sampl)
    for i in range(len(sampl)):
        for j in range(N):
            sampl[i].append(0)
    # print(sampl)
    for i in range(t):
        for j in range(N):
            sampl[i][j] = Bernoulli_discription(p)
    return sampl

def arrey_creation (N,t):
    sampl=[]
    for i in range(t):
        sampl.append(0)
    for i in range(len(sampl)):
        sampl[i] = []
    # print(sampl)
    for i in range(len(sampl)):
        for j in range(N):
            sampl[i].append(0)
    # print(sampl)
    return sampl

def CDF(p,c):
    if c < 0:
        g = 0
    elif 0 <= c and c < 1:
        g = 1-p
    elif c >= 1:
        g = 1
    return g

def CDF_arrey(p,sampl):
    yCDF = []
    for i in range(len(sampl)):
        yCDF.append(CDF(p,sampl[i]))
    return yCDF

def EDF (sampl):
    n: int =len(sampl[1])
    y_EDF = arrey_creation(n,len(sampl))
    work_samples = sampl

    for i in range(5):
        for j in range(n):
            if work_samples[i][j] <= work_samples[i][0]:
                y_EDF[i][j]=0
            elif work_samples[i][j] > work_samples[i][0] and work_samples[i][j] < work_samples[i][n-1]:
                y_EDF[i][j] = (j/n)
            else:
                y_EDF[i][j]=1
    return y_EDF



n = 100000
p = 0.7
N = n


x=[]
for i in range(n):
    x.append(Bernoulli_discription(p))


x.sort()
# print(x)

y = PMF(p,n,x)
# print(y)

plt.vlines(x,0,y)
plt.legend(title='N = {}'.format(n),loc="upper left")
plt.show()


sampl = sampaling(n,p,5)
# print(sampl)
for i in range(5):
    sampl[i].sort()
# print(sampl)


print('______________')
kvantilX=[]
for v in [0.1,0.5,0.7]:
    kvan = ceil(v*(n-1))
    if (kvan+1) < (v*n):
        kvantilX.append(sampl[0][kvan+1])
    elif (kvan + 1) == (v * n):
        kvantilX.append((sampl[0][kvan]+sampl[0][kvan+1])/2)
    elif (kvan+1) > (v*n):
        kvantilX.append(sampl[0][kvan])

gg=[0.1,0.5,0.7]
for i in range(3):
    print(kvantilX[i]," {}".format(gg[i]))



o=[]
a=[-1,0,1]
b=[0,1,2]
ss1=[]
cc=["red","green","blue","orange","brown"]



for i in range(5):
    sa = sampl[i]
    lenn = len(sa)
    t=sa.index(1)/lenn
    tt=[0,t,1]
    plt.hlines(tt,a,b,label='EDF{}'.format(i+1),colors=cc[i])


xCDF=np.arange(-5,5,0.01)
yCDF=[]

for i in range(len(xCDF)):
    yCDF.append(CDF(p,xCDF[i]))

xCDF.sort()


yCDF = CDF_arrey(p,xCDF)


plt.plot(xCDF,yCDF, color='black', label='CDF')

plt.legend(title='N = {}'.format(n))
plt.show()


for i in range(5):
    sampl[i].sort()


for i in range(5):
    plt.hist(sampl[i],color=cc[i],label="EHMF{:d}".format(i+1),alpha=0.5)



plt.legend(title='N = {}'.format(n))
plt.show()