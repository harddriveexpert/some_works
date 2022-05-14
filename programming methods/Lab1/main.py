import data_modul
import StudentClass
import time
import SortingModule
import datetime





print(datetime.datetime.now())
sampl = [100,500,1000,5000,10000,50000,100000]

for i in range(len(sampl)):
    print('\n' + '-----' + str(sampl[i]) + '-----')
    data_modul.creation_of_data(sampl[i])  # создаем файл с данными
    data_array = data_modul.creation_array(sampl[i])

    start2 = time.time()
    b = SortingModule.HeapSort(data_array)
    end2 = time.time()
    data_modul.write_data_info('HeapSort     ', start2 - end2, sampl[i])
    data_modul.write_data_info_live('HeapSort     ', start2 - end2, sampl[i])

    start3 = time.time()
    c = SortingModule.merge_sort(data_array)
    end3 = time.time()
    data_modul.write_data_info('merge_sort   ', start3 - end3, sampl[i])
    data_modul.write_data_info_live('merge_sort   ', start3 - end3, sampl[i])

    start1 = time.time()
    a = SortingModule.selection_sort(data_array)
    end1 = time.time()
    data_modul.write_data_info('election_sort', start1 - end1, sampl[i])
    data_modul.write_data_info_live('election_sort', start1 - end1, sampl[i])



Time = 0
data_modul.output_file(list(reversed(c)),Time)

print(datetime.datetime.now())