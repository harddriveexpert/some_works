import data_modul
from StudentClass import Student, Multimap
import time
import SortingModule
import datetime
import SearchModul
import copy

print(datetime.datetime.now())
findword = "Шварев"
sampl = [100, 500, 1000, 5000, 10000, 50000, 100000]

for i in range(len(sampl)):
    print('\n' + '-----' + str(sampl[i]) + '-----')
    data_modul.creation_of_data(sampl[i]) # создаем файл с данными
    data_array = data_modul.creation_array(sampl[i])




    start2 = time.time()
    b = SearchModul.direct_search(data_array,findword)
    end2 = time.time()

    data_modul.write_data_info('direct_search ', start2 - end2, sampl[i])
    data_modul.write_data_info_live('direct_search ', start2 - end2, sampl[i])





    start3 = time.time()
    c = SearchModul.binar_search_with_sortind(data_array,findword)
    end3 = time.time()

    data_modul.write_data_info('binar_search_with_sortind ', start3 - end3, sampl[i])
    data_modul.write_data_info_live('binar_search_with_sortind ', start3 - end3, sampl[i])






    start1 = time.time()
    a = SearchModul.binar_search(data_array,findword)
    end1 = time.time()

    data_modul.write_data_info('binar_search', start1 - end1, sampl[i])
    data_modul.write_data_info_live('binar_search', start1 - end1, sampl[i])





    merge = SortingModule.merge_sort(copy.deepcopy(data_array))
    multik = Multimap(merge)

    start4 = time.time()
    multik.find(findword)
    end4 = time.time()

    data_modul.write_data_info('multimap', start4 - end4, sampl[i])
    data_modul.write_data_info_live('multimap', start4 - end4, sampl[i])


print(datetime.datetime.now())