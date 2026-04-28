# Learning intentions:
# - Create a protected attribute
# - Create a private attribute

class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False

    def have_birthday(self):
        self.age += 1

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10)
print(p1)

#ACTIVITIES:
#1. Make category a private attribute than test to make sure it can't be changed once created
#2. Add another private attribute for breed