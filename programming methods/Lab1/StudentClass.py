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

    def __gt__(self, other):  # >
        if self.level > other.level:
            return True
        elif self.level == other.level:
            if self.name > other.name:
                return True
            elif self.name == other.name:
                if self.fac > other.fac:
                    return True
                elif self.fac == other.fac:
                    if self.spec > other.spec:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __lt__(self, other):  # <
        if self.level < other.level:
            return True
        elif self.level == other.level:
            if self.name < other.name:
                return True
            elif self.name == other.name:
                if self.fac < other.fac:
                    return True
                elif self.fac == other.fac:
                    if self.spec < other.spec:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __ge__(self, other):  # >=
        if self.level > other.level:
            return True
        elif self.level == other.level:
            if self.name > other.name:
                return True
            elif self.name == other.name:
                if self.fac > other.fac:
                    return True
                elif self.fac == other.fac:
                    if self.spec > other.spec:
                        return True
                    if self.spec == other.spec:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __le__(self, other):  # <=
        if self.level < other.level:
            return True
        elif self.level == other.level:
            if self.name < other.name:
                return True
            elif self.name == other.name:
                if self.fac < other.fac:
                    return True
                elif self.fac == other.fac:
                    if self.spec < other.spec:
                        return True
                    elif self.spec == other.spec:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False