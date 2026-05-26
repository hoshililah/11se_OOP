import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield, strength, agility, intelligence):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
        self.strength = strength 
        self.agility = agility 
        self.intelligence = intelligence 
  
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

    def skill_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
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


class Wizard(Fighter):
    def __init__(self,name, starting_health, weapon, shield,magic):
        super().__init__(name, starting_health, weapon, shield)
        self.magic = magic

    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power + self.magic


class Wizard(Fighter):
    def __init__(self,name, starting_health, weapon, shield,magic):
        super().__init__(name, starting_health, weapon, shield)
        self.magic = magic

    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power + self.magic
    
you = Fighter('You',100,60,20)
wiz = Wizard('The Grey Wizard',100,30,10,50)

you.report()
wiz.report()

while True:
    print('You attack the',wiz.name)
    wiz.defend(you.skill_attack())
    wiz.report()
    time.sleep(2)
    print('')
    if wiz.is_dead():
        print('You win')
        break
    print(wiz.name,'attacks you . . .')
    you.defend(wiz.random_attack())
    you.report()
    time.sleep(2)
    if you.is_dead():
        print(wiz.name,'wins')
        break
    print('')

class Fighter:
    def attack(self):
        return self.strength
    
class Mage(Fighter):
    def attack(self):
        return self.strength + self.intelligence 
    
class Ninja(Fighter):
    def attack(self):
        return self.strength + random.randint(10,30)

class Warrior(Fighter):
    def __init__(self, name):
        super().__init__(name, 140, 80, 10, 10)
        self.rage = 0 

    def heavy_attack(self):
        damage = random.randint(20,40) + self.rageself.rage =+ 5
        return damage 
    
    class Ninja(Fighter):
        def __init__(self,name):
            super().__init__(name, 90, 15, 70, 15)
            self.dodge_chance = 40

        def dodge(self):
            return random.randint(1,100) <= self.dodge_chance
        
class Mage(Fighter):
    def __init__(self, name):
        super().__init__(name, 80, 10, 10, 80)
        self.mana = 100

    def fireball(self):
        if self.mana >= 20:
            self.mana -= 20
            damage = random.randint(40,60)
            return damage 
        else:
            print("Not enough mana")
            return 0 
        
#Troll regeneration 
def regeneration(self):
    self.health += 10

#Gnome Trickery 
def confuse(self):
    chance = random.randint(1,100)
    if chance <= 30:
        print("The Gnome tricked you!")
        return True
    return False

#Python Venom 
class Fighter:
    def attack(self):
        return 10
    
    def attack(self):
        return random.randint(20,40)
    
#Ninja Attack
def attack(self):
    critical = random.randint(1,100)
    if critical <= 30:
        return random.randint(40,60)
    return random.randint(10,20)

#Mage Attack
def attack(self):
    if self.mana >= 20:
        self.mana -= 20
        return random.randint(35,55)
    return random.randint(5,10)