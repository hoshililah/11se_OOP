# Learning intentions:
# - Create a class pet with same information as in previous examples
# - Create an object instance of class pet

class Pet:
    def __init__(self, name, category, age, vaccinated, ccard, billing_address, owner_name, account_balance):
        self.name = name
        self.category = category 
        self.age = age 
        self.vaccinated = vaccinated
        self.ccard = ccard 
        self.billing_address = billing_address
        self.owner_name = 'unknown'
        self.account_balance = 0

p1 = Pet('Bonnie', 'Cat', '3', 'True', '3423 2326 7543 1234', '17 Park Drive', 'The Shire 3695', 129.95)
p2 = Pet('Foxy', 'Dog', '7', 'False', '0928 4289 2789 2389', '71 Long Street', 'The Other Shire 5963', 921.59)

p1.owner_name = 'Annie Jenkins'
p2.owner_name = 'Frannie Lenkins'

print()
print('p1')
print('---')
print(p1.name)
print(p1.category)
print(p1.age)
print(p1.vaccinated)
print(p1.ccard)
print(p1.billing_address)
print(p1.owner_name)
print(p1.account_balance)
print()

print('p2')
print('---')
print(p2.name)
print(p2.category)
print(p2.age)
print(p2.vaccinated)
print(p2.ccard)
print(p2.billing_address)
print(p2.owner_name)
print(p2.account_balance)
print()

#ACTIVITIES:
#1. Print out vaccination status of Bonnie
#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)