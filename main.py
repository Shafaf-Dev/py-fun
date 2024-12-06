# Mysterious Island Adventure Game
import time
import random


class Player:
    """Player class"""

    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.score = 0


class MysteriousIslandGame:
    """Mysterious Island Adventure Game"""

    def __init__(self):
        self.player = None
        self.game_over = False

    def start_game(self):
        print("🏝️ Welcome to the Mysterious Island Adventure! 🏝️")
        time.sleep(1)
        player_name = input("Enter your name: ")

        # Create a new player
        self.player = Player(player_name)

        self.introduction()

    def introduction(self):
        print(f"\nWelcome {self.player.name}!You've crashed on a mysterious island.")
        time.sleep(1)

        print("\nYou are mission to survive and escape the island.")
        time.sleep(1)

        self.main_game_loop()

    def main_game_loop(self):
        while not self.game_over:
            self.show_status()
            choice = self.get_player_choice()
            self.process_choice(choice)

    def show_status(self):
        print("\n--- GAME STATUS ---")
        print(f"Health: {'❤️ ' * (self.player.health // 20)}")
        print(
            f"Inventory: {', '.join(self.player.inventory) if self.player.inventory else 'Empty'}"
        )
        print(f"Score: {self.player.score}")

    def get_player_choice(self):
        print("\nWhat would you like to do?")
        print("1. Explore the forest")
        print("2. Search the beach")
        print("3. Climb a mountain")
        print("4. Rest and recover")
        print("5. Check inventory")

        while True:
            try:
                choice = int(input("Enter your choice (1-5): "))
                if 1 <= choice <= 5:
                    return choice
                else:
                    print("Invalid choice. Enter a number between 1 and 5.")
            except ValueError:
                print("Invalid choice. Enter a number between 1 and 5.")

    def process_choice(self, choice):
        if choice == 1:
            self.explore_forest()
        elif choice == 2:
            self.search_beach()
        elif choice == 3:
            self.climb_mountain()
        elif choice == 4:
            self.rest()
        elif choice == 5:
            self.check_inventory()

    def explore_forest(self):
        """Explore the forest"""
        print("\n🌳 You venture into the dense forest...")
        time.sleep(1)
        events = [
            self.find_treasure,
            self.encounter_wild_animal,
            self.discover_mysterious_artifact,
        ]

        random.choice(events)()

    def find_treasure(self):
        print("You found a treasure chest!")

        treasure = random.choice(["Golden Key", "Ancient Map", "Mysterious Gem"])
        self.player.inventory.append(treasure)
        print(f"You added {treasure} to your inventory!")
        self.player.score += 50

    def encounter_wild_animal(self):
        print("OH NO! A wild animal attacks you!")
        damage = random.randint(10, 30)
        self.player.health -= damage

        print(f"You lost {damage} health points!")

        if self.player.health <= 0:
            self.game_over = True
            print("You have died! Game Over!")

    def discover_mysterious_artifact(self):
        print("You discover a strange, glowing artifact!")
        self.player.score += 75
        print("Your curiosity grows and you feel a strange energy...")

    def search_beach(self):
        print("\n🏖️ You walk along the sandy beach...")
        time.sleep(1)

        events = [
            self.find_shipwreck,
            self.collect_shells,
            self.spot_rescue_boat,
        ]

        random.choice(events)()

    def find_shipwreck(self):
        print("You find an old shipwreck!")

        item = random.choice(["Rusty Compass", "Survival Kit", "Water Bottle"])
        self.player.inventory.append(item)
        print(f"You find a {item} in the wreckage")
        self.player.score += 40

    def collect_shells(self):
        print("You collect beautiful seashells.")
        self.player.score += 20

    def spot_rescue_boat(self):
        print("You spot a distant rescue boat!")
        time.sleep(1)
        if random.random() < 0.5:
            print("But it's too far away to signal...")
        else:
            print("You successfully signal the boat!")
            self.player.score += 100

    def climb_mountain(self):
        print("\n⛰️ You start climbing the rocky mountain...")
        time.sleep(1)
        difficulty = random.randint(1, 3)

        if difficulty == 1:
            print("The climb is easy! You reach the top quickly.")
            self.player.score += 60
        elif difficulty == 2:
            print("The climb is challenging. You lose some energy.")
            self.player.health -= 20
        else:
            print("The climb is treacherous! You slip and fall.")
            self.player.health -= 30

        if self.player.health <= 0:
            self.game_over_screen()

    def rest(self):
        heal_amount = random.randint(10, 30)
        self.player.health = min(100, self.player.health + heal_amount)
        print(f"\n😴 You rest and recover {heal_amount} health points!")

    def check_inventory(self):
        if not self.player.inventory:
            print("\nYour inventory is empty.")
        else:
            print("\n🎒 Your Inventory:")
            for item in self.player.inventory:
                print(f"- {item}")

    def game_over_screen(self):
        print("\n☠️ GAME OVER ☠️")
        print(f"Final Score: {self.player.score}")
        print("You were unable to survive the Mysterious Island...")
        self.game_over = True


def main():
    game = MysteriousIslandGame()
    game.start_game()


if __name__ == "__main__":
    main()
