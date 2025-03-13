# items.py
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name, f"A {name} dealing {damage} damage")
        self.damage = damage

class Potion(Item):
    def __init__(self, name, heal_amount):
        super().__init__(name, f"A {name} that heals {heal_amount} HP")
        self.heal_amount = heal_amount

    def use(self, character):
        if character.stats["health"] < character.stats["max_health"]:
            character.stats["health"] = min(character.stats["health"] + self.heal_amount, character.stats["max_health"])
            print(f"{character.name} used {self.name}, healing {self.heal_amount} HP!")
            return True
        print(f"{character.name} is already at full health!")
        return False