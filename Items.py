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
        if character.health < character.max_health:
            character.health = min(character.health + self.heal_amount, character.max_health)
            print(f"{character.name} used {self.name}, healing {self.heal_amount} HP!")
            return True
        print(f"{character.name} is already at full health!")
        return False