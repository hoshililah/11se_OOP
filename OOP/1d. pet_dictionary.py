#Tutorial 4 Dictionaries
#1 Create a Dictionary that stores pet information
#2 Change values within the dictionary
#3 Add values to the dictionary

print()

pet1 = {
'name' : 'Miss Bonnie',
'animal category' : 'Cat',
'age' : 4,
'vaccinated' : True,
'credit card' : '3423 2326 7543 1234',
'billing address' : '17 Park Drive, The Shire 3695',
'owner name' : 'Annie Jenkins',
'account balance' : 129.95,
}

pet1['age'] += 1

for item in pet1:
    print(item, ':',pet1[item])
print()

pet2 = {
'name' : 'Bingo',
'animal category' : 'Dog',
'age' : 7,
'vaccinated' : True,
'credit card' : '2456 4289 4289 1039',
'billing address' : '56 Long Street, The Other Shire 5963',
'owner name' : 'Frannie Lenkins',
'account balance' : 192.59,
}

for item in pet2:
    print(item, ':',pet2[item])
print()

#ACTIVITIES:
#1. Change name to Miss Bonnie
#2. Increase age by 1
#3. Create another pet who is a dog, fill in all the fields
