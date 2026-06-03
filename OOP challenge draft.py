import random, time

# ============================================
# FIGHTER BASE CLASS
# ============================================

class Fighter:
    """Base class for all fighters"""
    def __init__(self, name, fighter_class, health, attack, defense):
        self.name = name
        self.fighter_class = fighter_class
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
    
    def show_status(self):
        """Display fighter status"""
        print(f"\n{self.name} ({self.fighter_class}): {self.health}/{self.max_health} HP")
    
    def is_alive(self):
        """Check if fighter is still alive"""
        return self.health > 0
    
    def take_damage(self, damage):
        """Take damage, reduced by defense"""
        actual_damage = max(1, damage - self.defense)
        self.health -= actual_damage
        return actual_damage
    
    def basic_attack(self):
        """Basic attack - everyone can do this"""
        damage = self.attack + random.randint(5, 15)
        return damage


# ============================================
# PLAYER CHARACTER CLASSES
# ============================================

class Warrior(Fighter):
    """Strong attack, high defense"""
    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 8)
    
    def power_strike(self):
        """Special move: double damage"""
        damage = self.attack * 2 + random.randint(10, 20)
        print(f"⚔️  {self.name} uses POWER STRIKE!")
        return damage


class Mage(Fighter):
    """High attack with magic, low defense"""
    def __init__(self, name):
        super().__init__(name, "Mage", 80, 18, 4)
    
    def fireball(self):
        """Special move: high damage"""
        damage = self.attack * 2.5 + random.randint(15, 25)
        print(f"🔥 {self.name} casts FIREBALL!")
        return damage


class Ninja(Fighter):
    """Fast, moderate damage"""
    def __init__(self, name):
        super().__init__(name, "Ninja", 90, 16, 6)
    
    def shadow_strike(self):
        """Special move: high damage if lucky"""
        if random.randint(1, 100) < 60:  # 60% success rate
            damage = self.attack * 2.2 + random.randint(12, 22)
            print(f"💀 {self.name} uses SHADOW STRIKE!")
            return damage
        else:
            print(f"❌ {self.name}'s shadow strike MISSED!")
            return 0


class Paladin(Fighter):
    """Balanced - good defense and attack"""
    def __init__(self, name):
        super().__init__(name, "Paladin", 110, 14, 10)
    
    def heal(self):
        """Special move: restore health"""
        heal_amount = 25
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"✨ {self.name} uses HEAL (+{heal_amount} HP)!")
        return 0  # No damage


# ============================================
# ENEMY CLASSES
# ============================================

class Enemy(Fighter):
    """Base enemy class"""
    def __init__(self, name, fighter_class, health, attack, defense):
        super().__init__(name, fighter_class, health, attack, defense)


class Goblin(Enemy):
    """Weak enemy"""
    def __init__(self):
        super().__init__("Goblin", "Goblin", 40, 8, 2)


class Orc(Enemy):
    """Medium enemy"""
    def __init__(self):
        super().__init__("Orc", "Orc", 70, 12, 4)


class Troll(Enemy):
    """Strong enemy"""
    def __init__(self):
        super().__init__("Troll", "Troll", 100, 14, 6)


class Demon(Enemy):
    """Very strong enemy"""
    def __init__(self):
        super().__init__("Demon", "Demon", 110, 16, 5)


class Lich(Enemy):
    """Boss enemy"""
    def __init__(self):
        super().__init__("Lich", "Lich", 150, 18, 7)


# ============================================
# COMBAT SYSTEM
# ============================================

def battle(player, enemy):
    """Simple turn-based battle"""
    print(f"\n{'='*50}")
    print(f"⚔️  BATTLE: {player.name} vs {enemy.name}")
    print(f"{'='*50}")
    
    round_num = 1
    
    while player.is_alive() and enemy.is_alive():
        print(f"\n--- ROUND {round_num} ---")
        
        # Player's turn
        print(f"\n{player.name}'s turn!")
        print(f"1. Basic Attack")
        print(f"2. Special Move")
        
        while True:
            choice = input("Choose (1 or 2): ").strip()
            if choice in ['1', '2']:
                break
            print("❌ Invalid choice!")
        
        if choice == '1':
            damage = player.basic_attack()
            print(f"   Basic attack: {damage} damage")
        else:
            # Special move - depends on class
            if player.fighter_class == "Warrior":
                damage = player.power_strike()
            elif player.fighter_class == "Mage":
                damage = player.fireball()
            elif player.fighter_class == "Ninja":
                damage = player.shadow_strike()
            elif player.fighter_class == "Paladin":
                damage = player.heal()
                if damage == 0:
                    enemy.show_status()
                    player.show_status()
                    round_num += 1
                    continue  # Skip enemy turn if healing
        
        actual_damage = enemy.take_damage(damage)
        print(f"   {enemy.name} takes {actual_damage} damage!")
        
        if not enemy.is_alive():
            break
        
        # Enemy's turn
        print(f"\n{enemy.name}'s turn!")
        enemy_damage = enemy.basic_attack()
        print(f"   {enemy.name} attacks for {enemy_damage} damage!")
        
        actual_damage = player.take_damage(enemy_damage)
        print(f"   {player.name} takes {actual_damage} damage!")
        
        # Show status
        enemy.show_status()
        player.show_status()
        
        round_num += 1
        time.sleep(1)
    
    # Battle result
    print(f"\n{'='*50}")
    if player.is_alive():
        print(f"🎉 {player.name} wins!")
        return True
    else:
        print(f"💀 {player.name} was defeated!")
        return False


# ============================================
# MAIN GAME
# ============================================

def main():
    print("\n" + "="*60)
    print("🗡️  THE KINGDOM NEEDS A HERO 🗡️")
    print("="*60)
    
    print("""
The evil dark forces have invaded the kingdom!
Goblins, Orcs, Trolls, Demons, and the powerful Lich
are spreading chaos and destruction.

YOU must defeat them all and save the kingdom!

Will you rise to the challenge?
    """)
    
    input("[Press Enter to begin...]")
    
    # Choose class
    print("\n" + "="*60)
    print("CHOOSE YOUR CHARACTER")
    print("="*60)
    print("""
1. ⚔️  WARRIOR (High HP + Strong Attack)
2. 🔮 MAGE (High Attack + Fireball Special)
3. 🥷 NINJA (Fast + Shadow Strike Special)
4. ⚡ PALADIN (Balanced + Can Heal)
    """)
    
    class_map = {
        '1': Warrior,
        '2': Mage,
        '3': Ninja,
        '4': Paladin
    }
    
    while True:
        choice = input("Choose (1-4): ").strip()
        if choice in class_map:
            break
        print("❌ Invalid choice!")
    
    player_name = input("\nEnter your hero name: ").strip() or "Hero"
    player = class_map[choice](player_name)
    
    print(f"\n✅ Welcome, {player_name} the {player.fighter_class}!")
    player.show_status()
    
    # Game progression
    levels = [
        ("Level 1: Goblin Scouts", Goblin),
        ("Level 2: Orc Warriors", Orc),
        ("Level 3: Forest Trolls", Troll),
        ("Level 4: Demonic Servants", Demon),
        ("Level 5: The Ancient Lich (BOSS)", Lich),
    ]
    
    lives = 3
    
    for level_name, enemy_class in levels:
        print(f"\n{'='*60}")
        print(level_name)
        print(f"{'='*60}")
        print(f"Lives remaining: {lives}")
        
        enemy = enemy_class()
        won = battle(player, enemy)
        
        if won:
            print(f"✅ {level_name} COMPLETED!")
            # Heal player between levels
            player.health = player.max_health
            print(f"✨ You rest and recover your health...")
        else:
            lives -= 1
            print(f"⚠️  You were defeated!")
            
            if lives > 0:
                print(f"💪 You prepare for another attempt...")
                print(f"Lives remaining: {lives}\n")
                player.health = player.max_health  # Reset health
                
                # Retry this level
                while True:
                    retry = input("Try this level again? (yes/no): ").strip().lower()
                    if retry in ['yes', 'no', 'y', 'n']:
                        break
                
                if retry in ['yes', 'y']:
                    continue  # Retry this level
                else:
                    print("GAME OVER - You gave up!")
                    return
            else:
                print("💀 GAME OVER - NO LIVES LEFT")
                print("The kingdom falls to darkness...")
                return
    
    # Victory!
    print("\n" + "="*60)
    print("🎉 YOU SAVED THE KINGDOM! 🎉")
    print("="*60)
    print(f"""
Congratulations, {player_name} the {player.fighter_class}!

All the dark forces have been defeated!
The Lich is vanquished!
The kingdom is safe once more!

You are hailed as the greatest hero in the land.

                    *** THE END ***
    """)


if __name__ == "__main__":
    main()
