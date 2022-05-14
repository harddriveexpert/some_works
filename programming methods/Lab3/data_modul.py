import random
import StudentClass2
import StudentClass
import datetime

def creation_of_data(N):
    name = ['Шварев','Римский', 'Чайковский', 'Мусоргский', 'Бородин', 'Глинка', 'Скрябин','Рахманинов', 'Стравинский','Прокофьев','Шостакович','Шаплавский','Шимановский','Смирнов','Иванов','Кузнецов','Соколов','Попов','Лебедев','Козлов','Новиков','Морозов','Петров','Волков','Соловьёв','Васильев','Зайцев','Павлов','Семёнов','Голубев']
    fak = ['Факультет экономических наук','Московский институт электроники и математики им.А.Н. Тихонова','Факультет компьютерных наук','Высшая школа бизнеса','Факультет права','Высшая школа юриспруденции и администрирования','Факультет гуманитарныхнаук','Факультет социальных наук']
    spec = [['Департамент теоретической экономики','Департамент прикладнойэкономики','Департамент математики'],['Департамент электронной инженерии','Департамент компьютернойинженерии','Департамент прикладной математики'],['Департамент программной инженерии','Департамент анализа данных иискусственного интеллекта','Департамент больших данных и информационного поиска'],['Департамент бизнес-информатики','Департамент маркетинга','Департаментоперационного менеджмента и логистики'],['Департамент теории права и межотраслевых юридических дисциплин','Департаментпубличного права','Департамент частного права'],['Институт юридического менеджмента','Институт кадровогоадминистрирования','Институт спортивного менеджмента и права'],['Школа философии и культурологии','Школа филологических наук','Институтклассического Востока и античности'],['Департамент социологии','Департамент политики и управления','Департаментпсихологии']]
    f1=open('datd.txt','w')#создание файла с данными

    b = random.randint(0, N - 1)

    for i in range(N):
        fak_num = random.randint(0, len(fak) - 1)
        if i == b:
            f1.write('{}'.format(random.randint(100, 300)) + '|' + name[0] + '|' + fak[fak_num] + '|' + spec[fak_num][random.randint(0, 2)] + '\n')
        else:
            f1.write('{}'.format(random.randint(100,300))+ '|' + name[random.randint(1,len(name)-1)] + '|' + fak[fak_num] + '|' +spec[fak_num][random.randint(0,2)] + '\n')
    f1.close()

    return 0

def creation_array(N): #передача данных файла в массив
    f1 = open('datd.txt','r')
    data_array = []
    for i in range(N):
        line = f1.readline()
        data_array.append(StudentClass.Student(line))
    f1.close()
    return data_array

def creation_array2(N): #передача данных файла в массив
    f1 = open('datd.txt','r')
    data_array = []
    for i in range(N):
        line = f1.readline()
        data_array.append(StudentClass2.StudenL(line))
    f1.close()
    return data_array

def array_info(array): #вывод массива
    for i in range(len(array)):
        array[i].PrintInfo()
    return 0

def output_file(array,Time): #запись данных в файл
    f1 = open('data_output.txt','w')
    for i in range(len(array)):
        f1.write(array[i].PrintInfoSTR())
        f1.write("time:"+str(Time))
        f1.close()
    return 0

def write_data_info(word,time,sampl):
    f1=open('datd_info.txt','a')
    f1.write(str(word)+ '|' + str(time) + '|' + str(sampl) + '|' + str(datetime.datetime.now()) + '\n'+'\n')
    f1.close()
    return 0

def write_data_info_live(word,time,sampl):
    print(str(word) + '|' + str(time) + '|' + str(sampl) + '|' + str(datetime.datetime.now()) + '\n' +'_________')
    return 0