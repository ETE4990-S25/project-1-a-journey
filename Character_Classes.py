# character_classes.py

base_stats = {
    "Mage": {"health": 60, "max_health": 60, "strength": 20},
    "Assassin": {"health": 70, "max_health": 70, "strength": 50},
    "Knight": {"health": 100, "max_health": 100, "strength": 80},
    "Archer": {"health": 80, "max_health": 80, "strength": 60}
}

available_classes = ["Mage", "Assassin", "Knight", "Archer"]

class Character(object):
    def __init__(self, name, class_type):
        if class_type not in available_classes:
            raise ValueError(f"Invalid class type. Choose from {available_classes}")
        self.name = name
        self.class_type = class_type
        self.stats = base_stats[class_type].copy()
        self.inventory = []

    def display_stats(self):
        print(f"\nCharacter: {self.name} ({self.class_type})")
        print(f"Health: {self.stats['health']}/{self.stats['max_health']}")
        print(f"Strength: {self.stats['strength']}")
        print("Inventory: " + (", ".join(self.inventory) if self.inventory else "Empty"))

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, "Mage")

    def cast_spell(self, damage):
        # Simplified: No mana, just uses strength-based damage
        spell_damage = self.stats["strength"] + 10  # Bonus damage for spell
        print(f"{self.name} casts a spell, dealing {spell_damage} damage!")
        return spell_damage

class Assassin(Character):
    def __init__(self, name):
        super().__init__(name, "Assassin")

    def stealth_attack(self):
        # Simplified: Uses strength instead of agility
        damage = self.stats["strength"] // 2
        print(f"{self.name} performs a stealth attack, dealing {damage} damage!")
        return damage

class Knight(Character):
    def __init__(self, name):
        super().__init__(name, "Knight")

    def shield_block(self):
        block_amount = self.stats["strength"] // 3
        print(f"{self.name} raises their shield, blocking {block_amount} damage!")
        return block_amount

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, "Archer")

    def ranged_shot(self):
        # Simplified: Uses strength instead of agility
        damage = self.stats["strength"] // 2
        print(f"{self.name} fires an arrow, dealing {damage} damage!")
        return damage

def create_character(name, class_type):
    class_map = {"Mage": Mage, "Assassin": Assassin, "Knight": Knight, "Archer": Archer}
    if class_type not in class_map:
        raise ValueError(f"Invalid class type. Choose from {available_classes}")
    return class_map[class_type](name)