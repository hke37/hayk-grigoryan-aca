import random
import string

class Person:

    def __init__(self, fn, ln, a, g, idn):
        self.first_name = fn
        self.last_name = ln
        self.age = a
        self.gender = g
        self.id_number = idn


    def __str__(self):
        # print("Person")
        return "{} {} - {}, {}, \nID Number - {}".format(self.first_name, self.last_name, self.age, self.gender, self.id_number)

class Customer(Person):
    def __init__(self, fn, ln, a, g, idn, prof, ly):
        super().__init__(fn, ln, a, g, idn)
        self.profession = prof
        self.loyalty_years = ly
        self.acc_number = ''.join(random.choices(string.digits, k = 16))

    def __str__(self):
        # print("Customer")
        return "{}\n{} \nloyalty years - {}".format(super().__str__(), self.profession, self.loyalty_years)


# t = Customer("Gegham", "Jivanyan", 32, "Male", "AM0456778", "Programmer", 9)
# print(t)



