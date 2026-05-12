# Learning intentions:
# - Create a method (function belonging to a class)
# - Discuss the use of attributes in the method

class Pet:
    def __init__(self, name, category, age=0): 
        self.name = name 
        self.category = category 
        self.age = age 
        self.ccard = 'unknown' 
        self.vaccinated = False 
        
    def have_birthday(self): 
        self.age += 1 
        
    def __str__(self):
        payment_status = 'registered' if len(self.ccard) == 19 else 'unregistered'  
        vac_status = 'VACCINATED' if self.vaccinated else 'NOT VACCINATED'
        
        my_status = 'Name: ' + self.name + '\n' + \
                    'Category: ' + self.category + '\n' + \
                    'Age: ' + str(self.age) + '\n' + \
                    'Payment status: ' + payment_status + '\n' + \
                    'Vaccinated: ' + vac_status
        return my_status 

p1 = Pet('Bonnie', 'Cat', 10) 
p1.vaccinated = True 
p1.have_birthday() 
print(p1)

    

#ACTIVITIES:
#1. Add another method to vaccinate the pet
#2. Add another attribute for account balance then add a method to clear balance
#3. Add a method to print the animals age in human years use a multiplier of 7 if animal is a dog and a multiplier of 6 if it is a cat
# Use print statements to ensure you have comeplted each activity correctly.