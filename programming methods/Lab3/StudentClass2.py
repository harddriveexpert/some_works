import time


def easy_hash(key, size):
    hashnumber = 0
    for letter in key:
        hashnumber += ord(letter)
    return hashnumber % size


def hard_hash(key, size):
    hashnumber = 0
    for letter in key:
        hashnumber += ord(letter)
        hashnumber -= (hashnumber << 5) | (hashnumber >> 13)
    return hashnumber % size


class StudenL:
    level: int
    name: str
    fac: str
    spec: str
    my_hash_easy: int
    my_hash_hard: int

    def __init__(self, line: str):
        level, name, fac, spec = line.split('|')
        level = int(level)
        self.level = level
        self.name = name
        self.fac = fac
        self.spec = spec
        self.my_hash_easy = easy_hash(name, 1000000)
        self.my_hash_hard = hard_hash(name, 1000000)


class Hash :
    def __init__(self):
        self.size = 1000000
        self.count_easy = 0
        self.count_hard = 0
        self.key_easy = [None] * self.size
        self.data_easy = [[]] * self.size
        self.key_hard = [None] * self.size
        self.data_hard = [[]] * self.size

    def put(self, key, data_, hash_value, slots, data_array, count):
        if slots[hash_value] is None:
            slots[hash_value] = key
            data_array[hash_value] = [data_]
        else:
            if slots[hash_value] == key:
                data_array[hash_value].append(data_)
            else:
                next_slot, count = self.rehash(hash_value, len(slots), count)
                while slots[next_slot] is not None and slots[next_slot] != key:
                    next_slot, count = self.rehash(next_slot, len(slots), count)

                if slots[next_slot] is None:
                    slots[next_slot] = key
                    data_array[next_slot] = [data_]
                elif slots[next_slot] == key:
                    slots[next_slot] = key
                    data_array[next_slot].append([data_])
                else:
                    raise Exception('Мало места в таблице')
        return count

    def rehash(self, old_hash, size, count=None):
        if count is not None:
            count += 1
            return (old_hash + 1) % size, count
        return (old_hash + 1) % size

    def insert_of_data(self, obj: StudenL):
        self.count_easy = self.put(obj.name, obj, obj.my_hash_easy, self.key_easy, self.data_easy, self.count_easy)
        self.count_hard = self.put(obj.name, obj, obj.my_hash_hard, self.key_hard, self.data_hard, self.count_hard)

    def get(self, key, start_slot, slots, data):
        data_ = None
        stop = False
        found = False
        position = start_slot
        while slots[position] is not None and not found and not stop:
            if slots[position] == key:
                found = True
                data_ = data[position]
            else:
                position = self.rehash(position, len(slots))
                if position == start_slot:
                    stop = True
        return data_

    def value(self, key):
        hash_easy_ = easy_hash(key, self.size)
        start_easy = time.time()
        easy = self.get(key, hash_easy_, self.key_easy, self.data_easy)
        time.sleep(0.001)
        end_easy = time.time()

        hash_hard_ = hard_hash(key, self.size)
        start_hard = time.time()
        hard = self.get(key, hash_hard_, self.key_hard, self.data_hard)
        time.sleep(0.001)
        end_hard = time.time()

        if easy:
            return  easy[0].name, str(end_easy - start_easy).replace('.', ','), self.count_easy, hard[0].name, str(end_hard - start_hard).replace('.', ','), self.count_hard
        else:
            return "Ключ не найден", str(end_easy - start_easy), str(end_hard - start_hard)


