#Learning Intentions
#1. Create a defend method that helps you repel an attack
#2. Create a loop which simulates a fight and declares a winner
#3. Test the game 

import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield
  
   