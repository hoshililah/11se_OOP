import random, time 

#Base Fighter Class
class Fighter:
    def __init__(self,name, health, shield, strength, agility, intelligence):
        self.name = name
        self.__health = health
        self.shield = shield
        
        self.strength = strength 
        self.agility = agility 
        self.intelligence = intelligence 
  
#Display Health
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self):
        return self.__health <= 0

        
# Basic Attack
    def attack(self):
        damage = random.randint(
            self.strength//2,
            self.strength
        )
        print(self.name, "attacks for", damage)
        return damage 

#skill attack using timer
    def skill_attack(self):
        target = random.randint(2,6)
        print('Hit ENTER in exactly',target,'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = round(toc - tic)

# Successful Timing
        if time_taken == target:
            damage = self.attack() * 2
            print("Perfect!")
            print("Critical damage:", damage)
            return damage 
        else:
            print("Missed!")
            return self.attack()

#Defending
    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print(self.name, "takes", damage, "damage")
        else:
            print(self.name, "blocked the attack")

#WARRIOR CLASS
class Warrior(Fighter):
    def __init__(self,name):
        super().__init__(
            name, 
            140,  
            20, 
            80, 
            10, 
            10
        )
        self.rage = 0
# Special Warrior Attack
    def mega_attack(self):
        self.rage += 5
        damage = random.randint(20,40) + self.rage
        print(self.name, "uses MEGA ATTACK!")
        return damage

# NINJA CLASS
class Ninja(Fighter):
    def __init__(self, name):
        super().__init__(
            name, 
            90,  
            10, 
            15, 
            70, 
            15
        )
        self.dodge_chance = 40

# Ninja dodge ability
    def dodge(self):
        chance = random.randint(1,100)
        return chance <= self.dodge_chance

# Ninja critical attack
    def attack(self):
        critical = random.randint(1,100)
        if critical <= 30:
            damage = random.randint(40,60)
            print("CRITICAL HIT!")
            return damage 
        return random.randint(10,20)

#MAGE CLASS
class Mage(Fighter):
    def __init__(self,name):
        super().__init__(
            name, 
            80,  
            10, 
            10, 
            10, 
            80
        )
        self.mana = 100
    
# Magic Attack
    def attack(self):
        damage = random.randint(15,25)
        if self.mana >= 20:
            self.mana -= 20
            damage += 25
            print(self.name, "uses magic!")
            print("Mana remaining:", self.mana)
            return damage 
        else:
            print("The Mage is low on mana!")
        return damage

#TROLL CLASS
class Troll(Fighter):
    def __init__(self):
        super().__init__(
            "Troll", 
            120, 
            15, 
            80, 
            10, 
            10
        )
#Troll Regeneration
    def regeneration(self):
        self.__health += 10
        print("The Troll regernerates 10 health!")

#GNOME CLASS
class Gnome(Fighter):
    def __init__(self):
        super(). __init__(
            "Gnome", 
            80,  
            10, 
            10, 
            20, 
            70
        )
#Gnome Trick Ability
    def confuse(self):
        chance = random.randint(1,100)
        if chance <= 30:
            print("The Gnome tricks you!")
            return True
        return False

#SPERENT CLASS
class Serpent(Fighter):
    def __init__(self):
        super().__init__(
            "Serpent", 
            100,  
            10, 
            40, 
            20, 
            40
        )
        
#Instant strike mechanic
    def venom_strike(self):
        print("The Serpent prepares a venom strike!")
        print("Press ENTER in exactly 2 seconds!")
        tic = time.time()
        input()
        toc = time.time()
        time_taken = round(toc - tic)
        if time_taken != 2:
            print("The Serpent strikes!")
            return True
        print("You avoided the venom strike!")
        return False

# --------------------------------
# STORY INTRO
# --------------------------------

print()
print('WELCOME')
print()
print(""" 
      The king has fallen deathly ill after being poisoned by an ancient curse. 
    
      Only one cure exists.
    
      A legendary medicine made from:
    
      > Troll blood
      > Gnome beard moss
      > Serpent venom 
    
      You are the final warrior brave enough to travel through the cursed lands and gather the ingredients.
    
      But each creature of course does not want to die. 
      
      The troll relies on brute strength.
      The gnome uses intelligence and deception.
      The serpent waits silently for the perfect moment to strike.
      
      Failure means death.
       
      """)

print()
print("Choose your character.") 
print("""
      1. Warrior
      2. Ninja
      3. Mage 
      """)

print()
choice = input("Type the number of your chosen character: ")
if choice == "1":
    you = Warrior("Hero")
    print("You have chosen the Warror! Prepare for combat!")

elif choice == "2":
    you = Ninja("Hero")
    print("You have chosen the Ninja! Stealth and Agility are your allies.")

elif choice == "3":
    you = Mage("Hero")
    print("You have chosen the Mage! Will magic be the ultimate weapon?")

else:
    you = Warrior("Hero")
    print("Invalid choice. \n Your fate has been decided. \n Prepare for combat Warrior")


# ----------------------------
# Battle Function
# ----------------------------

def battle(you, enemy):

    while True:
        print()

    # Gnome confusion ability
        if isinstance(enemy, Gnome):
            if enemy.confuse():
                pass
            else:
                enemy.defend(you.skill_attack())
        else:
            enemy.defend(you.skill_attack())
        
        enemy.report()
        time.sleep(2)

    # Troll regeneration
        if isinstance(enemy, Troll):
            if random.randint(1,100) <= 30:
                enemy.regeneration()
            
            if enemy.is_dead():
                print()
                print("You defeated", enemy.name)
                return True
        
    # Serpent venom strike
        if isinstance(enemy, Serpent):
            if enemy.venom_strike():
                print("The venom kills you instantly!")
                return False
            
        print()
        print("Choose your attack: ")
        print("1. Normal Attack")
        print("2. Special Attack")

        attack_choice = input("Choice: ")
        
        # NORMAL ATTACK
        if attack_choice == "1":
            damage = you.skill_attack()

        # SPECIAL ABILITY
        elif attack_choice == "2":
            
            # Warruor special attack
            if isinstance(you, Warrior):
                damage = you.mega_attack()

            # Mage special attack
            elif isinstance(you,Mage):
                damage = you.attack()

            elif isinstance(you, Ninja):
                damage = you.attack()
            else:
                print("Invalid choice.")
                damage = you.attack()
            enemy.defend(damage)

        print(enemy.name, "attacks!")

        if isinstance(you, Ninja):
            if you.dodge():
                print("You dodged the attack!")
            else:
                you.defend(enemy.attack())

        if isinstance(you, Warrior):
            if you.mega_attack():
                print('You used MEGA attack!')
            else:
                you.defend(enemy.attack())
        

        you.report()
        time.sleep(2)

        if you.is_dead():
            print()
            print("You were defeated by", enemy.name)
            return False

# ----------------------------
# TROLL LEVEL
# ----------------------------

lives = 3     
while True:
    enemy = Troll()
    won = battle(you, enemy)
    if won:
        print()
        print("You collected Troll Blood!")
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
            print("You recover and prepare to fight again...")

# ----------------------------
# GNOME LEVEL
# ----------------------------

lives = 3    
while True:
    enemy = Gnome()
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
            print("You recover and prepare to fight again...")

# ----------------------------
# SERPENT LEVEL
# ----------------------------


enemy = Serpent()
won = battle(you, enemy)
if won:
    print()
    print("You collected Serpent Venom!")
else:
    print()
    print("The Serpents venom is fatal. You have failed your mission.")
    print("GAME OVER")
    quit()

# ----------------------------
# ENDING
# ----------------------------

print()
print("You have gathered all 3 ingredients!")
print("""
    The medicine is created...
    The King drinks the cure.
    The curse is broken!
    For your bravery, you are Knighted by the King.
    """)
print()
print('_____________________________________')
print()
print("THE END")

