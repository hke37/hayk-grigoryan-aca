class Person: 

    def __init__(self, fn, ln, a, g):
        self.first_name = fn
        self.last_name = ln
        self.age = a
        self.gender = g

    def __str__(self):
        print("Person")
        return "{} {} - {},{}".format(self.first_name, self.last_name, self.age, self.gender)

class Teacher(Person):
    def __init__(self, fn, ln, a, g, prof, exp):
        super().__init__(fn, ln, a, g)
        self.profession = prof
        self.experience = exp

    def __str__(self):
        print("Teacher")
        return "{}\n{} {}".format(super().__str__(), self.profession, self.experience)


t = Teacher("Gegham", "Jivanyan", 32, "Male", "Programmer", 9)
print(t)




#############################################################################


class Person:
    def __init__(self, fn, age):
        self.full_name = fn
        self.age = age
        self.gender = None

    def __str__(self):
        print("Person")
        if self.gender == "Female":
            return "{} - {}".format(self.full_name, self.gender)
        else:
            return "{} - {}, {}".format(self.full_name, self.age, self.gender)


class Student(Person):
    def __init__(self, fn, a, univ, fac):
        super().__init__(fn, a)
        self.university = univ
        self.faculty = fac

    def __str__(self):
        print("Student")
        return "{}, faculty of {}\n".format(self.university, self.faculty) + super().__str__()


s = Student("Julia Smith", 32, "YSU", "Informatics and Applied Mathematics")
print(s)


