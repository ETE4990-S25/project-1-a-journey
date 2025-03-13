# utils.py
import json

def save_game(character, filename="save_game.json"):
    data = {
        "name": character.name,
        "class_type": character.class_type,
        "stats": character.stats,
        "inventory": character.inventory
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Game saved to {filename}")

def load_game(filename="save_game.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        character = create_character(data["name"], data["class_type"])
        character.stats = data["stats"]
        character.inventory = data["inventory"]
        print(f"Game loaded from {filename}")
        return character
    except FileNotFoundError:
        print("No save file found.")
        return None