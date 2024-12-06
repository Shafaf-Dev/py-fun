import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.score = 0


class MysteriousIslandGameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Mysterious Island Adventure")
        master.geometry("600x500")
        master.configure(bg="#2c3e50")

        self.player = None
        self.game_over = False

        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        # Game Title
        self.title_label = tk.Label(
            self.master,
            text="Mysterious Island Adventure",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="white",
        )
        self.title_label.pack(pady=20)

        # Status Frame
        self.status_frame = tk.Frame(self.master, bg="#34495e")
        self.status_frame.pack(fill="x", padx=20, pady=10)

        # Health Label
        self.health_label = tk.Label(
            self.status_frame,
            text="Health: 100",
            font=("Arial", 12),
            bg="#34495e",
            fg="white",
        )
        self.health_label.pack(side="left", padx=10)

        # Score Label
        self.score_label = tk.Label(
            self.status_frame,
            text="Score: 0",
            font=("Arial", 12),
            bg="#34495e",
            fg="white",
        )
        self.score_label.pack(side="right", padx=10)

        # Inventory Label
        self.inventory_label = tk.Label(
            self.master,
            text="Inventory: Empty",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="white",
        )
        self.inventory_label.pack(pady=10)

        # Game Text Display
        self.game_text = tk.Text(
            self.master,
            height=10,
            width=70,
            font=("Courier", 10),
            bg="#ecf0f1",
            state="disabled",
        )
        self.game_text.pack(pady=10)

        # Button Frame
        self.button_frame = tk.Frame(self.master, bg="#2c3e50")
        self.button_frame.pack(pady=10)

        # Action Buttons
        actions = [
            ("Explore Forest", self.explore_forest),
            ("Search Beach", self.search_beach),
            ("Climb Mountain", self.climb_mountain),
            ("Rest", self.rest),
            ("Check Inventory", self.check_inventory),
        ]

        for text, command in actions:
            btn = tk.Button(
                self.button_frame,
                text=text,
                command=command,
                bg="#3498db",
                fg="white",
                font=("Arial", 10),
            )
            btn.pack(side="left", padx=5)

    def start_game(self):
        player_name = simpledialog.askstring(
            "Welcome", "Enter your name, brave explorer:", parent=self.master
        )
        if player_name:
            self.player = Player(player_name)
            self.update_status()
            self.display_text(
                f"Welcome, {player_name}! You've crashed on a mysterious island.\n"
                + "Your mission is to survive and escape!"
            )
        else:
            self.master.quit()

    def display_text(self, message):
        self.game_text.configure(state="normal")
        self.game_text.delete(1.0, tk.END)
        self.game_text.insert(tk.END, message)
        self.game_text.configure(state="disabled")

    def update_status(self):
        self.health_label.config(text=f"Health: {self.player.health}")
        self.score_label.config(text=f"Score: {self.player.score}")
        self.inventory_label.config(
            text=f"Inventory: {', '.join(self.player.inventory) if self.player.inventory else 'Empty'}"
        )

    def explore_forest(self):
        events = [
            self.find_treasure,
            self.encounter_wild_animal,
            self.discover_mysterious_artifact,
        ]
        random.choice(events)()

    def find_treasure(self):
        treasure = random.choice(["Golden Key", "Ancient Map", "Mysterious Gem"])
        self.player.inventory.append(treasure)
        self.display_text(
            f"You found a treasure chest!\nYou added {treasure} to your inventory!"
        )
        self.player.score += 50
        self.update_status()

    def encounter_wild_animal(self):
        damage = random.randint(10, 30)
        self.player.health -= damage
        self.display_text(
            f"OH NO! A wild animal attacks you!\nYou lost {damage} health points!"
        )
        self.update_status()

        if self.player.health <= 0:
            self.game_over_screen()

    def discover_mysterious_artifact(self):
        self.display_text("You discover a strange, glowing artifact!")
        self.player.score += 75
        self.update_status()

    def search_beach(self):
        events = [self.find_shipwreck, self.collect_shells, self.spot_rescue_boat]
        random.choice(events)()

    def find_shipwreck(self):
        item = random.choice(["Rusty Compass", "Survival Kit", "Water Bottle"])
        self.player.inventory.append(item)
        self.display_text(
            f"You find an old shipwreck!\nYou found a {item} in the wreckage!"
        )
        self.player.score += 40
        self.update_status()

    def collect_shells(self):
        self.display_text("You collect beautiful seashells.")
        self.player.score += 20
        self.update_status()

    def spot_rescue_boat(self):
        if random.random() < 0.5:
            self.display_text(
                "You spot a distant rescue boat, but it's too far away to signal..."
            )
        else:
            self.display_text("You successfully signal the rescue boat!")
            self.player.score += 100
        self.update_status()

    def climb_mountain(self):
        difficulty = random.randint(1, 3)

        if difficulty == 1:
            self.display_text("The climb is easy! You reach the top quickly.")
            self.player.score += 60
        elif difficulty == 2:
            self.display_text("The climb is challenging. You lose some energy.")
            self.player.health -= 15
        else:
            self.display_text("The climb is extremely tough!")
            self.player.health -= 30

        self.update_status()

        if self.player.health <= 0:
            self.game_over_screen()

    def rest(self):
        heal_amount = random.randint(10, 30)
        self.player.health = min(100, self.player.health + heal_amount)
        self.display_text(f"You rest and recover {heal_amount} health points!")
        self.update_status()

    def check_inventory(self):
        if not self.player.inventory:
            self.display_text("Your inventory is empty.")
        else:
            self.display_text(
                "Your Inventory:\n"
                + "\n".join(f"- {item}" for item in self.player.inventory)
            )

    def game_over_screen(self):
        messagebox.showinfo(
            "Game Over",
            f"Game Over!\nFinal Score: {self.player.score}\n"
            + "You were unable to survive the Mysterious Island...",
        )
        self.master.quit()


def main():
    root = tk.Tk()
    game = MysteriousIslandGameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
