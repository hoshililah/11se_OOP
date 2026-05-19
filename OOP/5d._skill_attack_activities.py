#Learning Intentions
#1. Create a skill attack method
#2. Use the time library to set up a timing measure (skill factor)
#3. Have the skill increase or decrease the final attack value

import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self):
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power
    
    def skill_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        target = random.randint(2,6)
        print('Hit enter in exactly',target,'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(target-time_taken)
        if multiplier < 2:
            multiplier = 0

        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')


you = Fighter('You',100,60,20)
troll = Fighter('Troll',300,30,10)

you.report()
troll.report()

while True:
    print('You attack the troll')
    troll.defend(you.skill_attack())
    troll.report()
    time.sleep(1)
    print('')
    if troll.is_dead():
        print('You win')
        break 
    print('The troll attacks you . . .')
    you.defend(troll.random_attack())
    you.report()
    time.sleep(1)
    if you.is_dead():
        print('The troll wins')
        break 
    print('')

