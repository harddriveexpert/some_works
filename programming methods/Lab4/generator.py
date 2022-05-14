import datetime
from time import sleep,time
from testmodul import *
import random

def get_value():
    return datetime.datetime.now().microsecond

def generator_of_array_LKN(size,m,k,b):
    sleep(0.001)
    r0 = (get_value())%100
    array = []
    for i in range(size):
        r1 = ((k * r0 + b) % m) % 10000
        r0 = r1
        array.append(r1)
    return array

def generator_of_array(size,m,k1,k2,b):
    sleep(0.001)
    r0 = (get_value())%100
    array = []
    for i in range(size):
        r1 = ((k1 * r0**2 + k2 * r0 + b) % m) % 10000
        r0 = r1
        array.append(r1)
    return array

def generator_of_array_random(size):
    a = []
    for i in range(size):
        a.append(random.randint(0,10000))
    return a

def generation_of_sampls(m, k, b):
    sempl1 = []
    sempl2 = []

    for i in range(10):
        sempl1.append(generator_of_array_LKN(50,m,k,b))
        sempl2.append(generator_of_array(50,m,k,k+7,b))
    print(sempl1)
    print(sempl2)

    print('\n\n------1-------')
    for i in range(len(sempl1)):
        print('\nНомер выборки:', i+1)
        test_of_array(sempl1[i])

    print('\n\n------2-------')
    for i in range(len(sempl2)):
        print('\nНомер выборки:', i + 1)
        test_of_array(sempl2[i])
    return 0

def test_of_speed(size,m,k,b):
    for i in size:
        start_time1 = time()
        generator_of_array_LKN(i,m,k,b)
        time1 = time() - start_time1

        start_time2 = time()
        generator_of_array(i, m, k,k+7,b)
        time2 = time() - start_time2

        start_time3 = time()
        generator_of_array_random(i)
        time3 = time() - start_time3

        print('\n------',i,'------')
        print('Время работы линейного конгруэнтного метода',time1)
        print('\nВремя работы квадратичныйконгруэнтного метода', time2)
        print('\nВремя работы Python', time3)
    return 0
