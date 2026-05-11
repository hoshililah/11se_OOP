# Learning intentions:
# - Create a list of pets
# - Use a for loop to print out various information about pets

class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.ccard) == 19:
            payment_status = 'registered'
    
        my_status = 'Name: ' + self.name + '\nCategory: ' + self.category +  '\nAge: ' + str(self.age) + '\nPayment Status: ' + payment_status + '\nVaccinated: ' + str(self.vaccinated)
        return my_status
    

p1 = Pet('Bonnie', 'Cat', '3')
p2 = Pet('Clyde', 'Dog', '7')
p3 = Pet(category = 'Rabbit', name = 'Bill', age = 13)
p4 = Pet('George', 'Cat', '6')
p5 = Pet('Sally', 'Hampster', '2')

pets = [p1, p2, p3, p4]
pets.append(p5)

for pet in pets:
    pet.vaccinated = True
    print(pet)
    print('')

p1.ccard = '2455 2309 2903 0964'

#ACTIVITIES:
#1. Add another pet to the list (try different methods)
#2. Vaccinate each pet in the list