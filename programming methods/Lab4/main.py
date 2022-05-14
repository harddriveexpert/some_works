from generator import *

m = (2**31) - 1
k = 1220703125
b = 7


generation_of_sampls(m,k,b)

print('-----------Тест скорости-----------')
size = [1000,5000,10000,50000,100000,250000,500000,750000,1000000]

test_of_speed(size,m,k,b)