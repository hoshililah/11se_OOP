import random
import time

class Fighter:
    def __init__(self, name, health, strength, agility, intelligence, defense):
        self.name = name
        self._health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.defense = defense
        self.dodging = False

    def report(self):
        print(f"{self.name}: Health: {self._health}")

    def restore_health(self):
        self._health = 100

    def is_dead(self):
        return self._health <= 0

    def random_attack(self):
        return self.strength + random.randint(5, 20)

    def attack(self):
        return self.random_attack()

    def skill_attack(self):
        target = random.randint(2, 6)
        print('Hit Enter in exactly', target, 'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        
        accuracy = max(0, 1 - abs(time_taken - target))
        attack_stat = self.agility + self.intelligence + random.randint(10, 25)
        
        if abs(time_taken - target) <= 0.15:
            damage = self.attack() * 2
            print("Perfect timing!")
            print("Critical damage:", damage)
            return damage
            
        damage = int(attack_stat * accuracy)
        print(f'Attack power: {damage}')
        return damage

    def defend(self, attack_power):
        if self.dodging:
            print(self.name, "dodges the attack!")
            self.dodging = False
            return 
            
        damage = max(0, int(attack_power) - self.defense)
        if damage == 0:
            print("Your attack did no damage!")
        else:
            print("Damage:", damage)
            self._health -= damage

    @staticmethod
    def allocate_points():
        points_left = 100
        strength = 0
        agility = 0
        intelligence = 0
        print("\nCreate your Character:")
        print("Allocate 100 points to:")
        print("- Intelligence\n- Strength\n- Agility")
        
        while True:
            print("\nPoints remaining:", points_left)
            intelligence = int(input("Intelligence: "))
            if intelligence > points_left:
                print("Not enough points")
                continue
            points_left -= intelligence
            break
            
        while True:
            print("\nPoints remaining:", points_left)
            strength = int(input("Strength: "))
            if strength > points_left:
                print("Not enough points")
                continue
            points_left -= strength
            break
            
        agility = points_left
        print("\nAgility automatically gets:", agility)
        return strength, agility, intelligence


# WARRIOR CLASS
class Warrior(Fighter):
    def __init__(self, name, strength, agility, intelligence):
        super().__init__(name, 100, strength, agility, intelligence, 20)
        
    def rage_strike(self):
        print(self.name, "uses Rage Strike!")
        return self.skill_attack() * 2


# NINJA CLASS
class Ninja(Fighter):
    def __init__(self, name, strength, agility, intelligence):
        super().__init__(name, 100, strength, agility, intelligence, 20)
        
    def shadow_dodge(self):
        print(self.name, "uses Shadow Dodge!")
        chance = random.randint(1, 60) + (self.agility // 2)
        if random.randint(1, 100) <= chance:
            self.dodging = True
            print("Dodge ready for the enemy's next turn!")
            return True
        else:
            print("Dodge failed!")
            return False


# MAGE CLASS
class Mage(Fighter):
    def __init__(self, name, strength, agility, intelligence):
        super().__init__(name, 100, strength, agility, intelligence, 20)
        self.mana = 100
        
    def fireball(self):
        if self.mana >= 30:
            self.mana -= 30
            damage = self.intelligence + random.randint(20, 40)
            print(self.name, "casts Fireball!")
            return damage
        print("Not enough Mana!")
        return self.attack()


# ENEMY CLASSES
class Troll(Fighter):
    def __init__(self, name):
        super().__init__(name, 100, 80, 10, 10, 20)
        
    def smash_attack(self):
        damage = int(self.strength * 1.5)
        print(self.name, "uses Smash Attack!")
        return damage


class Gnome(Fighter):
    def __init__(self, name):
        super().__init__(name, 100, 30, 40, 30, 20)
        
    def trickster(self):
        print(self.name, "uses Trickster Spell!")
        return int(self.agility + self.intelligence + random.randint(10, 30))


class Serpent(Fighter):
    def __init__(self, name):
        super().__init__(name, 100, 30, 30, 40, 20)
        
    def venom_strike(self):
        print("The Serpent prepares a venom strike!")
        print("Press ENTER in exactly 2 seconds!")
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        if 1.8 < time_taken < 2.2:
            print("You avoided the venom strike!")
            return 0
        print("The Serpent bites you with deadly venom!")
        return 999


# STORY INTRO
print("\n______________________________________\n")
print('WELCOME')
print("______________________________________\n")
print("""The king has fallen deathly ill after being poisoned by an ancient curse.
Only one cure exists. A medicine made from:
- Troll blood
- Gnome beard moss
- Serpent venom

You are the final warrior brave enough to gather the ingredients.
The troll relies on brute strength, the Gnome on Trickery.
And the most powerful of all, The Serpent, can kill you in an instant.
""")

print("Choose your character.\n")
print("1. Warrior\n2. Ninja\n3. Mage\n")
choice = input("Type the number of your chosen character: ")

if choice == "1":
    print("You have chosen the Warrior!")
elif choice == "2":
    print("You have chosen the Ninja!")
elif choice == "3":
    print("You have chosen the Mage!")
else:
    print("Invalid choice. Defaulting to Warrior.")
    choice = "1"

strength, agility, intelligence = Fighter.allocate_points()

if choice == "1":
    you = Warrior("Hero", strength, agility, intelligence)
elif choice == "2":
    you = Ninja("Hero", strength, agility, intelligence)
else:
    you = Mage("Hero", strength, agility, intelligence)


def battle(player, enemy):
    while True:
        print('')
        player.report()
        enemy.report()
        
        print("\n1. Basic Attack")
        print("2. Special/Skill Attack")
        choice_action = input("> ")
        
        # Players Turn
        if choice_action == "1":
            damage = player.attack()
        elif choice_action == "2":
            if isinstance(player, Warrior):
                damage = player.rage_strike()
            elif isinstance(player, Mage):
                damage = player.fireball()
            elif isinstance(player, Ninja):
                player.shadow_dodge()
                damage = player.attack()  # Ninja attacks normally after establishing dodge frame
            else:
                damage = player.attack()
        else:
            print("Invalid Action! Defaulting to Basic Attack.")
            damage = player.attack()
            
        enemy.defend(damage)
        
        if enemy.is_dead():
            print(f"\nYou defeated {enemy.name}!")
            return True
            
        # Enemys Turn
        if isinstance(enemy, Troll):
            attack_power = enemy.smash_attack() if random.randint(1, 100) <= 30 else enemy.random_attack()
        elif isinstance(enemy, Gnome):
            attack_power = enemy.trickster() if random.randint(1, 100) <= 30 else enemy.random_attack()
        elif isinstance(enemy, Serpent):
            attack_power = enemy.venom_strike()
        else:
            attack_power = enemy.random_attack()
            
        player.defend(attack_power)
        
        if player.is_dead():
            print(enemy.name, "defeated you!")
            return False


# LEVEL GAME LOOP ENGINE
levels = [
    {"name": "Level 1: Defeat the Troll.", "class": Troll, "monster": "Troll", "item": "Troll Blood"},
    {"name": "Level 2: Defeat the Gnome.", "class": Gnome, "monster": "Gnome", "item": "Gnome Beard Moss"},
    {"name": "Final Level: Defeat the Serpent.", "class": Serpent, "monster": "Serpent", "item": "Serpent Venom"}
]

for lvl in levels:
    print(f"\n{lvl['name']}")
    lives = 2
    while lives > 0:
        enemy_instance = lvl["class"](lvl["monster"])
        won = battle(you, enemy_instance)
        
        if won:
            print(f"You collected {lvl['item']}!")
            you.restore_health()
            if hasattr(you, 'mana'):
                you.mana = 100
            break
        else:
            lives -= 1
            print("Lives remaining:", lives)
            if lives == 0:
                print("GAME OVER")
                quit()
            you.restore_health()
            if hasattr(you, 'mana'):
                you.mana = 100

print("\nTHE END - The kingdom is saved!")
