import csv
import mimesis
import random


def city(numb):
    array = []
    array2 = []
    for i in range(numb):
        array.append(mimesis.Address().city())
    b = list(set(array))
    for j in range(len(b)):
        array2.append([str(j), b[j]])
    return array2


def generate_person(city, num):
    g = mimesis.Person('en')
    array = []
    for i in range(num):
        a = mimesis.Datetime().datetime(start=1950, end=2005)
        city_id = random.randrange(1, len(city) - 1)
        array.append([str(i), g.last_name(), g.name(), g.name(),  str(a.month) + '-' + str(a.day) + '-' + str(a.year),
                      str(city_id), g.gender(iso5218=False, symbol=False)])
    return array


def country(numb):
    array = []
    array2 = []
    for i in range(numb):
        array.append(mimesis.Address().country())
    b = list(set(array))
    for j in range(len(b)):
        array2.append([str(j), b[j]])
    return array2


def film_ganer():
    ganer = ['Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Thriller', 'Western']
    array = []
    for i in range(len(ganer)):
        array.append([str(i), ganer[i]])
    return array


def studio(num, city):
    g = mimesis.Person('en')
    array = []
    for i in range(num):
        city_id = random.randrange(0, len(city) - 1)
        array.append([str(i), g.name(), str(city_id)])
    return array


def actors(person):
    array = []
    for i in range(0, (len(person) // 2)):
        array.append([str(i)])
    return array


def directors(person):
    array = []
    for i in range((len(person) // 2), len(person)-1):
        array.append([str(i)])
    return array


def actor_s_role():
    role = ['Background Actor', 'Series regular', 'Recurring', 'Guest star', 'Co-star/day player', 'Cameo']
    array = []
    for i in range(len(role)):
        array.append([str(i), role[i]])
    return array


def actor_s_role_actors(actor, role):
    array = []
    for i in range(1, len(actor)):
        role_id = random.randrange(0, len(role) - 1)
        array.append([role_id, actor[i][0]])
    return array


def movi(num, country, diretors):
    g = mimesis.Person('en')
    array = []
    for i in range(num):
        a = mimesis.Datetime().datetime(start=1950, end=2022)
        direcors_id = random.randrange(1, len(diretors) - 1)
        contry_id = random.randrange(0, len(country) - 1)
        budget = random.randrange(0, 1000000000)
        array.append(
            [str(i), g.name(), int(a.year), str(contry_id), str(diretors[direcors_id][0]),
             str(budget)])
    return array


def contracts(actors, studio, movis, num):
    array = []
    for i in range(num):
        studio_id = random.randrange(0, len(studio) - 1)
        movi_id = random.randrange(1, len(movis) - 1)
        a = mimesis.Datetime().datetime(start=1950, end=2022)
        actors_id = random.randrange(0, len(actors) - 1)
        budget = random.randrange(0, 100000000)
        array.append(
            [str(i), str(studio_id),str(movis[movi_id][0]), str(a.month) + '-' + str(a.day) + '-' + str(a.year), str(actors_id),
             str(budget)])
    return array


def film_geners_movies(movi, ganer):
    array = []
    for i in range(0, len(movi)-1):
        ganer_id = random.randrange(0, len(ganer) - 1)
        array.append([str(ganer_id), str(i)])
    return array


def pr_all():
    print(cit)
    print(person)
    print(country_array)
    print(film_gan)
    print(studio_table)
    print(actor)
    print(directors_table)
    print(rol)
    print(actor_s_role_actors_table)
    print(movi_table)
    print(contract_table)
    print(film_geners_movies_table)


def write_to_csv(path, array):
    with open(path, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in array:
            writer.writerow(row)

def write_to_txt(path, array):
    f = open(path, 'w')
    for row in array:
        line = ''
        for i in range(len(row)):
            line = line + str(row[i])
            if i != len(row)-1:
                line += '|'
        f.write(line + '\n')




num_of_people = 1000
cit = city(num_of_people // 10)
write_to_txt('./csv/city_table.txt', cit)
person = generate_person(cit, num_of_people)
write_to_txt('./csv/person_table.txt', person)
country_array = country(num_of_people // 20)
write_to_txt('./csv/country_table.txt', country_array)
film_gan = film_ganer()
write_to_txt('./csv/film_gan_table.txt', film_gan)
studio_table = studio(50, cit)
write_to_txt('./csv/studio_table.txt', studio_table)
actor = actors(person)
write_to_txt('./csv/actor.txt', actor)
directors_table = directors(person)
write_to_txt('./csv/directors_table.txt', directors_table)
rol = actor_s_role()
write_to_txt('./csv/rol.txt', rol)
actor_s_role_actors_table = actor_s_role_actors(actor, rol)
write_to_txt('./csv/actor_s_role_actors_table.txt', actor_s_role_actors_table)
movi_table = movi(num_of_people // 10, country_array, directors_table)
write_to_txt('./csv/movi_table.txt', movi_table)
contract_table = contracts(actor, studio_table, movi_table, len(movi_table) * 10)
write_to_txt('./csv/contract_table.txt', contract_table)
film_geners_movies_table = film_geners_movies(movi_table, film_gan)
write_to_txt('./csv/film_geners_movies_table.txt', film_geners_movies_table)

# pr_all()
