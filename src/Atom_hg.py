class UnknownAtomError(Exception):
    def __init__(self, msg):
        self.__message = msg

    def get_info(self):
        return "not correct - {}".format(self.__message)


class Atom:

    ATOM_TYPES = ["C", "N", "H", "O", "P"]

    def __init__(self, name):
        try:
            if name not in Atom.ATOM_TYPES:
                raise UnknownAtomError("Atom Name")
        except UnknownAtomError as err:
            print(err.get_info())
        else:
            self.__name = name

    # def __add__(self, other):
    #     x = []
    #     x.append(self.__name)
    #     x.append(other.__name)
    #     return Molecule(x)

    def __str__(self):
        return "Atom Name: {} ".format(self.__name)



class Molecule:
    def __init__(self, list):
        self.__list = list

    def __add__(self, other):
        x = self.__list.append(other.__name)
        return x

    def __str__(self):
        return "molecule consists of {} ".format(self.__list)

##################
a1 = Atom("N")
m1 = Molecule(["H","H","O"])
print(m1 + a1)



# print(m1)
# print(m1.__dict__)










