# [3:30 PM] Patient / Doctor - Create a patient class and a doctor class.
# Have a doctor that can handle multiple patients and setup a scheduling program
# where a doctor can only handle 16 patients during an 8 hr work day.
# Patient class
# 	Data members:
# 		name - string
# 		surname - string
# 		age - integer from 18 to 100
# 		gender - ‘M’ or ‘F’
#            Data methods:
# 		constructor
#                         repr - “{name} {surname} - {gender}, {age} years old.”
#                         __ne__
# Doctor class
# 	Data members:
# 		name - string
# 		surname - string
# 		shedule - dictionary with {datetime: Patient}
#        	Data methods
# 		constructor
# 		repr - “Doctor {Name} {Surname} schedule
# 				{schedule}(every pair from new line)
# 		register patient(patient, datetime) - should add {datetime: patient}
# 		pair to schedule and print “Patient {patient} successfully registered
# 		at {datetime}”.  Check if patient already registered, and is that time free
# 		for doctor.
# 		Other case print appropriate messages - “Patient {patient}
# 		already registered” or “Datetime {datetime} already taken from {patient} patient”.
# 	is_free(datetime) - check if doctor free for given datetime
# 	p.s take into account that every patient take 30min from doctor
# is_registered(patient) - check if patient registered already

from datetime import datetime

class Patient:

    def __init__(self, n, sn, a, g):
        self.__name = n
        self.__surname = sn
        self.__age = a
        self.__gender = g

    def __repr__(self):
        return "{} {} - {}, {}".format(self.__name,self.__surname, self.__gender, self.__age)


class Doctor:

    def __init__(self, n, sn, sh):
        self.__name = n
        self.__surname = sn
        self.__schedule = sh

    def __repr__(self):
        return "Doctor {} {} - {}\n".format(self.__name, self.__surname, self.__schedule)

    def register(self, dt, p):
        if dt not in self.__shedule.keys() and p not in self.__schedule.values():
            self.__schedule[dt] = p
            print("Patient {} successfully registered at {}".format(dt,p))
            return self.__schedule
        else:
            print("Datetime {} already taken from {} patient".format(dt,self.__schedule[dt]))

    def check_datetime(self, dt):
        if dt not in self.__schedule.keys():
            print("datetime is free")
            return dt
        else:
            print("datetime is not available for register")



####################################

p1 = Patient("Valod", "Valodyan", 50, "M")
print(p1)
dt1 = datetime(2022,6,22,5,30,00)
print(dt1)
d1 = Doctor("Armen", "Armenyan", {dt1:p1})
print(d1)

# a = d1.register(datetime(2022,6,22,5,30,00),p1)



