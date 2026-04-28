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
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power

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

