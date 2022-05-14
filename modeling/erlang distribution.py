import random
from math import exp
from math import e
from math import log
from math import factorial
from math import ceil
import matplotlib.pyplot as plt
from scipy.special import gamma as gm
import numpy as np
import numpy as np2
from scipy.stats import gamma
import numpy as np




def erlang(a,l):
    i=1
    p=1
    while(i!=a):
        i=i+1
        u=random.random()
        p=p*u
    return -log(p)/l

def PDF(x,l,k):
    j = (l**(k) * x**(k-1) * e**(-x*l))/(factorial(k-1))
    return j

def CDF(i,l,k):
    sum1 = 0
    for j in range(0,k - 1):
        sum1 = sum1 + (((exp(-(l * i))) * ((l * i) ** j)) / (factorial(j)))
    return 1 - sum1

def sampaling (N,a,l,t):
    sampl=[]
    for i in range(t):
        sampl.append(0)
    for i in range(len(sampl)):
        sampl[i] = []
    for i in range(len(sampl)):
        for j in range(N):
            sampl[i].append(0)
    for i in range(t):
        for j in range(N):
            sampl[i][j] = erlang(a,l)
    return sampl

def arrey_creation (N,t):
    sampl=[]
    for i in range(t):
        sampl.append(0)
    for i in range(len(sampl)):
        sampl[i] = []
    for i in range(len(sampl)):
        for j in range(N):
            sampl[i].append(0)
    return sampl

def EDF (sampl):
    n =len(sampl[0])
    y_EDF = arrey_creation(n,len(sampl))
    work_samples = sampl

    for i in range(len(sampl)):
        for j in range(n):
            if work_samples[i][j] <= work_samples[i][0]:
                y_EDF[i][j]=0
            elif work_samples[i][j] > work_samples[i][0] and work_samples[i][j] < work_samples[i][n-1]:
                y_EDF[i][j] = (j/n)
            else:
                y_EDF[i][j]=1
    return y_EDF

def discard(sampl):
    x1 = []

    for i in range(len(sampl)):
        if (0 <= round(sampl[i], 1)) and (round(sampl[i], 1) <= 6):
            x1.append(round(sampl[i], 1))
    return x1

def difference_modulus(s1,s2):
    en=[]
    for i in range(len(s1)):
        en.append(abs(s1[i]-s2[i]))
    return max(en)

def xi (n,s1,s2):
    xi = 0
    nu = 1000
    for i in range(len(s2)):
        xi += ((s1[i] - s2[i] * n) ** 2) / (s2[i] * n)
    return xi

def rround (sampl):
    sampl1 = sampl
    for i in range(len(sampl)):
        for j in range(len(sampl1[i])):
            sampl1[i][j] = round(sampl1[i][j], 0)
    return sampl1

def EPMF (sampl):
    yv = arrey_creation(n, len(sampl))

    sss = rround(sampl)

    for i in range(len(sampl)):
        for j in range(len(sss[i])):
            yv[i][j] = (sampl[i]).count(sss[i][j]) / len(sampl[i])

    return yv



n=int(input())


k=5
l=1

x =[]
y=[]

for i in range(n):
    x.append(erlang(k,l))

x.sort()

for i in range(n):
    y.append(PDF(x[i],l,k))

print(x)
print(y)

plt.plot(x,y,label ='PDF')
plt.legend(title='N = {}'.format(n))
plt.show()

print('__________________________________')

sampl = sampaling(n,k,l,5)
print(sampl)

for i in range(len(sampl)):
    sampl[i].sort()
print(sampl)

y_EDF = EDF(sampl)
print(y_EDF)




xCDF=[]
yCDF=[]
for i in range(20):
    xCDF.append(i)
xCDF.sort()


for i in range(len(xCDF)):
    yCDF.append(CDF(i,l,k))


for i in range(5):
    plt.step(sampl[i], y_EDF[i],label="EDF {}".format(i+1))

plt.plot(xCDF, yCDF,color='black',label ='CDF' )
plt.legend(loc="upper left",title='N = {}'.format(n))
plt.show()


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

print('______________')

print(gamma.ppf(0.1,4))
print(gamma.ppf(0.5,4))
print(gamma.ppf(0.7,4))

fgfg = sampaling(n,k,l,5)
for i in range(5):
    plt.hist(fgfg[i],label='EHMF {}'.format(i+1))
plt.legend(title='N = {}'.format(n))
plt.show()






sampling_freq = rround(sampl)

yv = EPMF(sampl)


for i in range(5):
    plt.step(sampling_freq[i],yv[i], label='EPMF ' + str(i + 1))


xs=[]
ys=[]
zz=0
for i in range(200):
    zz += 0.1
    xs.append(zz)
for i in range(len(xs)):
    ys.append(PDF(xs[i],1,4))

plt.plot(xs,ys,color='black',label = 'PDF')


plt.legend(title='N = {}'.format(n))
plt.show()
