import math

def expected_value (array):
    r = 0
    for i in range(len(array)):
        r += array[i]
    return r/len(array)

def variance (array):
    expevalue = expected_value(array)
    d = 0
    for i in range(len(array)):
        d += (array[i]-expevalue)**2
    return d/len(array)

def standard_deviation (array):
    return variance(array)**(1/2)

def variation (array):
    return variance(array)**(1/2) / expected_value(array) * 100

def chia(array):
    b = sorted(array)
    k = math.ceil(math.log2(len(array))+1)
    step = 10000/k
    p = 1/k
    frequency = []
    for i in range(k):
        counter = 0
        for j in b:
            if (j > i*step) and (j <= (i+1)*step):
                counter += 1
            else:
                continue
        frequency.append(counter)
    chi = 0
    for i in range(k):
        chi += ((frequency[i] - p*len(b))**2) / (p*len(b))
    return chi

def test_of_array(array):
    print('----------------')
    print('Матожидание: ', expected_value(array),' | Дисперсия: ', variance(array), '\nВариация: ', variation(array), ' | Хи-квадрат', chia(array))
    print('----------------')
    if (chia(array) >= 0.18) and (chia(array) <=16.8):
        print("равномерное распределение")
    else:
        print("не равномерное распределение")

    if (variation(array) < 33):
        print("выборка однородна")
    else:
        print("выборка не однородна")
    return 0

