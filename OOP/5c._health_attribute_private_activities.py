#Learning Intentions
#1. Make health private (it becomes __health)
#2. Use methods to check if the fighter object is dead

import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.health))



    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.health -= damage
            print('Damage:', damage)
        else:
            print('No damage')


you = Fighter('You',100,60,20)
troll = Fighter('Troll',200,30,10)
