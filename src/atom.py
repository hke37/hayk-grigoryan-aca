from collections import Counter

class UnknownAtomError(Exception):
    def __init__(self, value):
        self.__value = value
        # print('class UnknownAtomError - constructor')

    def get_info(self):
        # print('class UnknownAtomError - getting')
        return "Invalid atom name - {}".format(self.__value)



class Atom:
    
    ATOMS = {'O': 'Oxygen', 'H': 'Hydrogen', 'N': 'Nytrogen', 'P': 'Phosphorius', 'C': 'Carbon'}

    def __init__(self, name):
        self.__is_valid = False
        try:
            if name not in self.ATOMS:
                raise UnknownAtomError(name)
        except UnknownAtomError as err:
            print(err.get_info())

        else:
            self.__name = name
            self.__is_valid = True
        # print('Atom class - constructor')


    @property
    def is_valid(self):
        return self.__is_valid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, x):
        if x in self.ATOMS:
            self.__name = x
        else:
            print("Object not changed")

    def __repr__(self):
        try:
            return self.ATOMS[self.__name]
        except AttributeError:
            return "Object does not created"

    def __add__(self, other):
        # print('atom class - addition method')
        return Molecul([self, other])


class Molecul:

    def __init__(self, a):
        self.__atoms = self.__check_atoms(a)

    def __check_atoms(self, l):
        v = []
        for x in l:
            if x.is_valid:
                v.append(x)
        return v

        
    @property
    def atoms(self):
        return self.__atoms
    
    @atoms.setter
    def atoms(self, b):
        self.__atoms = b


    def __add__(self, other):
        # print('Molecul class - addition')
        if isinstance(other, Atom):
            self.__atoms.append(other)
        else:
            self.__atoms.extend(other.atoms)
        return Molecul(self.__atoms)


    def __repr__(self):
        # print('molecul class - repr' )
        s = ''
        l =[]
        for i in self.__atoms:
            l.append(i.name)
        x = dict(Counter(l))
        for item in x:
            if x[item] == 1:
                s += str(item)
            else:
                s += str(item) + str(x[item])
        return "molecul: {}".format(s)

####################################################
#USER

a1 = Atom('H')
print(a1)
a2 = Atom('O')
a3 = Atom('C')
a4 = Atom('N')
a5 = Atom('P')
print(a1 + a2)
a6 = Atom('K')
print(a6)

m1 = Molecul([a1, a3, a1, a2, a4, a1, a2, a5, a5])
m2 = Molecul([a2, a3, a4, a2, a2, a5])
m3 = m1 + m2
print(m3)
m4 = m3 + a1
print(m4)
m5 = m3 + m4
print(m5)

m6 = m5 + a6 + a5
print(m6)