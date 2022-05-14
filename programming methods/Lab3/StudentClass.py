import time


class Student:
    level: int
    name: str
    fac: str
    spec: str

    def __init__(self,line):
        level,name,fac,spec = line.split('|')
        level = int(level)
        self.level = level
        self.name = name
        self.fac = fac
        self.spec = spec

    def PrintInfo(self):
        print(self.level,'|',self.name,'|',self.fac,'|',self.spec)

    def PrintInfoSTR(self):
        return str(str(self.level) + '|' + self.name + '|' + self.fac + '|' + self.spec)

    def __lt__(self, other):  #  <
        if self.name < other.name:
            return True
        else:
            return False

    def __le__(self, other):  #  <=
        if self.name == other.name:
            return True
        elif self.name < other.name:
            return True
        else:
            return False

    def __gt__(self, other):  #  >
        if isinstance(other, str):

            if self.name > other:
                return True
            else:
                return False
        else:
            if self.name > other.name:
                return True
            else:
                return False

    def __ge__(self, other):  #  >=
        if self.name == other.name:
            return True
        elif self.name > other.name:
            return True
        else:
            return False

    def __eq__(self, other):  #  ==
        if self.name == other:
            return True
        else:
            return False



class Multimap():
    multarr = []


    def __init__(self, array):
        self.multarr = []
        self.keys=[]
        for elem in array:
            self.multarr.append((elem.name, elem))

    def PrintInfoMM(self):
        print(self.multarr)

    def find(self, find_word):
        midel = len(self.multarr) // 2
        start = 0
        end = len(self.multarr) - 1
        while find_word != self.multarr[midel][0] and start <= end:
            if self.multarr[midel][0] > find_word:
                end = midel - 1
            else:
                start = midel + 1
            midel = (end + start) // 2
        time.sleep(0.001)
        if end >= start:
            return midel
        else:
            return -1
