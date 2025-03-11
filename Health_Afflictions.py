class Items(object):
    def __init__(self, name, max_health, health):
        self.name = name
        self.max_health = max_health
        self.health = health

class Healing(Items):
    def __init__(self, name, max_health, health):
        super().__init__(self, name, max_health, health)

    def heal_player(self, healing):
        if self.health < self.max_health:
            self.health = min(self.health + healing, self.max_health)
            print(f"{self.name} healed for {healing} HP. Current health: {self.health}/{self.max_health}")
        else:
            print(f"{self.name} is already at full health!")

class Poison(Items):
    def __init__(self, name, max_health, health):
        super().__init__(self, name, max_health, health)

    def do_damage(self, name, max_health, health):
        self.health = max(self.health - Poison)

player = Healing("Hero", 100, 50)
player.heal_player(15)  
player.heal_player(25)  