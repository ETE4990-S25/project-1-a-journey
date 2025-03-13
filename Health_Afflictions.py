# Health_Afflictions.py
class Items(object):
    def __init__(self, name, max_health, health):
        self.name = name
        self.max_health = max_health
        self.health = health

class Healing(Items):
    def __init__(self, name, max_health, health):
        super().__init__(name, max_health, health)  # Corrected: No extra 'self'

    def heal_player(self, healing):
        if self.health < self.max_health:
            self.health = min(self.health + healing, self.max_health)
            print(f"{self.name} healed for {healing} HP. Current health: {self.health}/{self.max_health}")
        else:
            print(f"{self.name} is already at full health!")

class Poison(Items):
    def __init__(self, name, max_health, health):
        super().__init__(name, max_health, health)  # Corrected: No extra 'self'

    def do_damage(self, damage):  # Fixed: Removed unused parameters 'name, max_health, health'
        self.health = max(self.health - damage, 0)  # Fixed: 'damage' instead of 'Poison'
        print(f"{self.name} took {damage} poison damage. Current health: {self.health}/{self.max_health}")

# Test code (optional, remove if not needed in the file)
if __name__ == "__main__":
    player = Healing("Hero", 100, 50)
    player.heal_player(15)
    player.heal_player(25) 