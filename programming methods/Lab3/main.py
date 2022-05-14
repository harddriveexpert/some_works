import data_modul
from StudentClass2 import Hash


findword = "Шварев"
sampl = [100, 500, 1000, 5000, 10000, 50000, 100000]

for j in range(len(sampl)):
    data = []
    asd = Hash()
    data_modul.creation_of_data(sampl[j])
    data_array = data_modul.creation_array2(sampl[j])

    for i in range(len(data_array)):
        asd.insert_of_data(data_array[i])

    print('\n' + '-----' + str(sampl[j]) +  '-----')

    print(asd.value(findword))