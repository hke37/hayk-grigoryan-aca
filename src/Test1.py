# Ստեղծել Length կլաս։ Երկարության հիմնական միավորը կհամարենք մետրը։ Կլասը պետք է ունենա որոշակի
# ինֆորմացիա, թե ինչպես
# փոխակերպել այլ միավորը մետրի (feet, km, yard, mile etc.)
#    a) Ստեղծել բառարան, որը կպահի վերոնշյալ ինֆորմացիան։ Բանալիները կլինեն միավորների անունները, իսկ արժեքները կլինեն
#    այն գործակիցները, որոնց օգնությամբ այդ միավորից ստանում ենք մետր։
#    b) Կլասը պետք է ունենա երկու instance attributes։ Երկարության արժեքը և միավորը։
#    c) Մենք պետք է կարողանանք երկարությունները իրար գումարել։ Սահմանել համապատասխան մեթոդը։ Ուշադրություն դարձնել
#    միավորներին։ Մենք չենք կարող ուղղակիորեն մետրը գումարել մղոնի կամ հակառակը։
#    d) Սահմանել __str__ մեթոդը։ Այս մեթոդը մեզ ցույց կտա օբյեկտի երկարությունը մետրերով։
#    e) Սահմանել __repr__ մեթոդը։ Այս մեթոդը մեզ ցույց կտա օբյեկտի երկարությունը այն միավորով, որով սահմանվել է։
# Լրացուցիչ, կարող եք ավելացնել հավելյալ տրամաբանություն որտեղ ճիշտ կգտնեք։



class Length:

    UNITS = {"METER": 1, "FEET": 0.3, "KM": 1000, "YARD": 0.9, "MILE": 1600}

    def __init__(self, u, v):
        self.__unit = u
        self.__value = v

    def get_value(self):
        return self.__value

    def get_unit(self):
        return self.__unit

    def __add__(self, other):
        x = self.__value
        if self.__unit == other.__unit:
            x += other.__value
        else:
            rate = self.UNITS[other.__unit] / self.UNITS[self.__unit]
            x += (rate * other.__value)
        return Length(self.__unit, x)

    def __repr__(self):
        return "{} {}".format(self.__value, self.__unit)

###########################################

a = Length("METER", 100)
print(a)
b = Length("KM", 200)
print(b)
c = a + b
print(c)
d = Length("YARD", 1000)
print( a + d)



















