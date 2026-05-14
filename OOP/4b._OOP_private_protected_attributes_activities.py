# Learning intentions:
# - Create a protected attribute
# - Create a private attribute

class Pet:
    def __init__(self, name, category, breed, age = 0):
        self.name = name
        self.category = category
        self.__breed = breed
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False

    def set_name(self,new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            print('Please use a string as a name attribute')
        

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.ccard) == 19:
            payment_status = 'registered'
    
        my_status =  '\nName: ' + self.name + '\nCategory: ' + self.category +  '\nAge: ' + str(self.age) + '\nPayment Status: ' + payment_status + '\nVaccinated: ' + str(self.vaccinated) + '\nBreed: ' + self.__breed + '\n'
        return my_status

p1 = Pet(name = 'Bonnie', category = 'Cat', breed = 'Tabby', age = 10)

p1.__breed = 'Red'
p1.set_name('Bonnifer')
print(p1)

#ACTIVITIES:
#1. Make category a private attribute than test to make sure it can't be changed once created
#2. Add another private attribute for breed