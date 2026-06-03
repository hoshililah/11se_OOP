import random, time 

class Fighter:
    def __init__(self,name,health,strength,agility,intelligence,defense):
        self.name = name
        self.__health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.defense = defense
        self.dodging = False
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self):
        if self.__health <= 0:
            return True
        else:
            return False
        
    # Health Points
    def heal(self, amount):
        self.__health += amount
        print(self.name, "heals for", amount, "health points.")

    def random_attack(self):
        attack_power = self.strength + random.randint(5,20)
        return attack_power

    def attack(self):
        return self.random_attack()

    def skill_attack(self):
        target = random.randint(2,6)
        print('Hit Enter in exactly',target,'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(target-time_taken)
        attack = self.agility + self.intelligence + random.randint(10,25)
        if multiplier < 2: 
            multiplier = 0
        if time_taken == target:
            damage = self.attack() * 2
            print("Perfect!")
            print("Damage:", int(damage))
            return damage 
        else:
            damage = int(attack*multiplier)
            print(f'Attack power: {damage}')
            return damage

    def defend(self, attack_power):
        if self.dodging:
            print(self.name, "dodges the attack!")
            self.dodging = False
            return
        damage = max(1, attack_power - self.defense)
        self.__health -= damage
        print("Damage: ", damage)


#WARRIOR CLASS
class Warrior(Fighter):
    def __init__(self,name):
        super().__init__(
            name, 
            100,
            70,  
            15, 
            15,
            50, 
        )

# Warrior Special Attack
    def rage_strike(self):
        print(self.name, "uses Rage Strike!")
        damage = self.skill_attack() * 2
        return damage

# NINJA CLASS
class Ninja(Fighter):
    def __init__(self,name):
        super().__init__(
            name,
            100,
            30,
            40,
            30,
            50
        )

# Ninja Special Attack
    def shadow_dodge(self):
        print(self.name, "uses Shadow Dodge!")
        chance = 50 + (self.agility//2) 
        if random.randint(1,100) <= chance:
            self.dodging = True
            print("Dodge successful!")
        else:
            print("Dodge failed!")

class Mage(Fighter):
    def __init__(self,name):
        super().__init__(
            name,
            100,
            20,
            20,
            60,
            50
        )
        self.mana = 100
    
# Mage Special Attack
    def fireball(self):
        if self.mana >= 30:
            self.mana -= 30
            damage = self.intelligence + self.mana//2
            print(self.name, "casts Fireball!")
            return damage 
        else:
            print("Not enough Mana!")
            return self.attack()
    
# ENEMY CLASS

# Troll Class
class Troll(Fighter):
    def __init__(self,name):
        super().__init__(
            name,
            100,
            80,
            10,
            10,
            50
        )

# Troll Special Attack
    def smash_attack(self):
        damage = self.strength * 1.5
        print(self.name, "uses Smash Attack!")
        return damage

# GNOME CLASS
class Gnome(Fighter):
    def __init__(self,name):
        super().__init__(
            name,
            100,
            30,
            40,
            30,
            50,
        )

# Gnome Special Attack
    def trickster(self):
        print(self.name, "uses Trickster Spell!")
        return int(self.agility + self.intelligence + random.randint(10,30))

# CLASS SERPENT
class Serpent(Fighter):
    def __init__(self,name):
        super().__init__(
            name,
            100,
            30,
            30,
            40,
            50,
        )

# Serpent Special Attack
    def venom_strike(self):
        print("The Serpent prepares a venom strike!")
        print("Press ENTER in exactly 2 seconds!")

        tic = time.time()
        input()
        toc = time.time()
       
        time_taken = (toc - tic)
        
        if 1.8 < time_taken < 2.2:
            print("The Serpent strikes!")
            return True 
        
        print("You avoided the venom strike!")
        return False


# STORY INTRO

print()
print("______________________________________")
print()
print('WELCOME')
print("______________________________________")
print(""" 
The king has fallen deathly ill after being poisoned by an ancient curse. 
    
Only one cure exists.
    
A legendary medicine made from:
    
    - Troll blood
    - Gnome beard moss
    - Serpent venom 
    
You are the final warrior brave enough to travel through the cursed lands and gather the ingredients.
      
The troll relies on brute strength.
The gnome uses intelligence and trickery.
The serpent waits is the most powerful of all, and at any moment can strike you with its deadly venom.
      
Failure means death.
      
Will you rise to the challenge, and save the Kingdom?
       
""")

print("Choose your character.") 
print("""
      1. Warrior
      2. Ninja
      3. Mage 
      """)

choice = input("Type the number of your chosen character: ")
print()
if choice == "1":
    you = Warrior("Hero")
    print("You have chosen the Warrior! ")

elif choice == "2":
    you = Ninja("Hero")
    print("You have chosen the Ninja!")

elif choice == "3":
    you = Mage("Hero")
    print("You have chosen the Mage!")

else:
    you = Warrior("Hero")
    print("Invalid choice. \nYour fate has been decided. \nYou are a Warrior!")

time.sleep(2)

def battle(player,enemy):
    while True:
        print('')
        player.report()
        enemy.report()
        print('')
        print("1. Attack")
        print("2. Special Attack")

        choice = input("> ")
        if choice == "1":
            damage = player.skill_attack()

        elif choice == "2":
            
            if isinstance(player, Warrior):
                damage = player.rage_strike()

            elif isinstance(player, Mage):
                damage = player.fireball()

            elif isinstance(player, Ninja):
                player.shadow_dodge()
                damage = 0
        else: 
            damage = player.skill_attack()

        enemy.defend(damage)
        enemy.report()

        if enemy.is_dead():
            print()
            print('You defeated', enemy.name, '!')
            return True

        if isinstance(enemy, Troll):
            if random.randint(1,100) <= 30:
                attack = enemy.smash_attack()
            else:
                attack = enemy.random_attack()
        
        elif isinstance(enemy, Gnome):
            if random.randint(1,100) <= 30:
                attack = enemy.trickster()
            else:
                attack = enemy.random_attack()
        
        elif isinstance(enemy, Serpent):
            if random.randint(1,100) <= 30:
                attack = enemy.venom_strike()
            else:
                attack = enemy.random_attack()
        
        else:
            attack = enemy.random_attack()

        player.defend(attack)

        if player.is_dead():
            print(enemy.name,'defeated you!')
            return False                    

# _____________
# TROLL LEVEL

print()
print("Level 1: You must defeat the Troll and collect its blood.")
print()
lives = 2
while True:     
    enemy = Troll("Troll")
    won = battle(you, enemy)
    if won:
        print()
        print("You collected the Troll Blood!")
        print()
        break
    else:
        lives -= 1
        print()
        print("Lives remaing:", lives)

        if lives == 0:
            print()
            print("The Troll has defeated you again.")
            print("You have failed in your mission.")
            print("GAME OVER")
            quit()
        else:
            print()
            print("Prepare to fight again...")

# _____________
# GNOME LEVEL

print()
print("Level 2: You must defeat the Gnome and collect the moss from its Beard.")
print()

lives = 2    
while True:
    enemy = Gnome("Gnome")
    won = battle(you, enemy)
    if won: 
        print()
        print("You collected Gnome Beard Moss!")
        break
    else:
        lives -= 1
        print()
        print("Lives remaing:", lives)

        if lives == 0:
            print()
            print("The Gnome has defeated you again.")
            print("You have failed in your mission.")
            print("GAME OVER")
            quit()
        else:
            print()
            print("Prepare to fight again...")

# ______________
# SERPENT LEVEL

print()
print("Final Level: You must defeat the Serpent and collect its Venom.")
print()

enemy = Serpent("Serpent")
won = battle(you, enemy)
if won:
    print()
    print("You collected Serpent Venom!")
else:
    print()
    print("The Serpents venom is fatal. You have failed your mission.")
    print("GAME OVER")
    quit()

# ___________
# ENDING

print()
print("You have gathered all 3 ingredients!")
print("""
\nThe medicine is created...
The King drinks the cure.

The curse is broken!

For your bravery, you are Knighted by the King.
""")
print('_____________________________________')
print()
print("THE END")
