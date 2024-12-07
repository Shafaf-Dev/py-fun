import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from PIL import Image, ImageTk
import os
import random


def main():
    root = tk.Tk()
    MysteriousIslandAdventureGUI(root)
    root.mainloop()


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.score = 0


class MysteriousIslandAdventure:
    def __init__(self, master):
        self.master = master
        master.title("Mysterious Island Adventure")
        master.geometry("600x500")
        master.configure(bg="#2c3e50")
        self.player = None
        self.game_over = False

        # Initialize these attributes to prevent AttributeError
        self.health_bar = None
        self.health_label = None
        self.score_label = None
        self.inventory_label = None
        self.game_text = None

        self.start_game()

    def start_game(self):
        player_name = simpledialog.askstring(
            "Welcome", "Enter your name, brave explorer:", parent=self.master
        )
        if player_name:
            self.player = Player(player_name)
            self.update_status()
            self.display_text(
                f"Welcome {player_name}! You've crashed on a mysterious island.\n"
                + "Your mission is to survive and escape!"
            )
        else:
            self.master.quit()

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
            self.display_text("The climb is easy! You reach the top quickly")
            self.player.score += 60
        elif difficulty == 2:
            self.display_text("The climb is challenging. You lose some energy")
            self.player.health -= 20
        else:
            self.display_text("The climb is extremely tough!")
            self.player.health -= 40

        self.update_status()

        if self.player.health <= 0:
            self.game_over_screen()

    def rest(self):
        heal_amount = random.randint(10, 20)
        self.player.health = min(100, self.player.health + heal_amount)
        self.display_text(f"You rest and recover {heal_amount} health points!")
        self.update_status()

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
        damage = random.randint(10, 40)
        self.player.health -= damage
        self.display_text(
            f"OH NO! A wild animal attacks you!\n You lose {damage} health points!"
        )
        self.update_status()

        if self.player.health <= 0:
            self.game_over_screen()

    def discover_mysterious_artifact(self):
        self.display_text("You discover a strange, glowing artifact!")
        self.player.score += 65
        self.update_status()

    def display_text(self, message):
        if hasattr(self, 'game_text'):
            self.game_text.configure(state="normal")
            self.game_text.delete(1.0, tk.END)
            self.game_text.insert(tk.END, message)
            self.game_text.configure(state="disabled")

    def update_status(self):
        # Update health (either progress bar or label)
        if hasattr(self, 'health_bar'):
            self.health_bar['value'] = self.player.health
        if hasattr(self, 'health_label'):
            self.health_label.config(text=f"Health: {self.player.health}")
        
        # Update score
        if hasattr(self, 'score_label'):
            self.score_label.config(text=f"Score: {self.player.score}")
        
        # Update inventory
        if hasattr(self, 'inventory_label'):
            self.inventory_label.config(
                text=f"Inventory: {', '.join(self.player.inventory) if self.player.inventory else 'Empty'}"
            )

    def game_over_screen(self):
        messagebox.showinfo(
            "Game Over", 
            f"Game Over!\nFinal Score: {self.player.score}\n"
            + "You were unable to survive the Mysterious Island..."
        )
        self.master.quit()


class MysteriousIslandAdventureGUI(MysteriousIslandAdventure):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title("Mysterious Island Adventure")
        master.geometry("800x600")
        master.configure(bg="#2c3e50")

        # Load resources
        self.load_resources()

        # Create UI elements
        self.create_background()
        self.create_status_bar()
        self.create_game_area()
        self.create_action_buttons()
        self.create_inventory_display()

    def load_resources(self):
        # Create a resources directory.
        os.makedirs("game_resources", exist_ok=True)

        # Load images
        self.images = {
            "background": self.load_default_image((800, 400), "#87CEEB"),  # Sky blue background
            "inventory_icon": self.load_default_image((30, 30), "#2ecc71"),  # Green icon
            "health_icon": self.load_default_image((30, 30), "#e74c3c"),  # Red icon
            "score_icon": self.load_default_image((30, 30), "#f39c12"),  # Orange icon
        }

    def load_default_image(self, size, color):
        """Create a default colored image if no image is found"""
        from PIL import Image, ImageDraw
        
        image = Image.new('RGBA', size, color)
        return ImageTk.PhotoImage(image)

    def load_image(self, filename, size):
        """Loading and resizing the image"""
        try:
            img_path = os.path.join("game_resources", filename)
            image = Image.open(img_path)
            image = image.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading image {filename}: {e}")
            # Return a default image if loading fails
            return self.load_default_image(size, "#3498db")

    def create_background(self):
        # Create a canvas for the background.
        self.canvas = tk.Canvas(
            self.master, width=800, height=400, bg="#2c3e50", highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        # Display the background image.
        self.canvas.create_image(400, 200, image=self.images["background"])

    def create_status_bar(self):
        # Status Frame
        status_frame = tk.Frame(self.master, bg="#34495e", height=50)
        status_frame.pack(fill="x")

        # Health section
        health_frame = tk.Frame(status_frame, bg="#34495e")
        health_frame.pack(side="left", padx=10)

        health_icon = tk.Label(
            health_frame, image=self.images["health_icon"], bg="#34495e"
        )
        health_icon.pack(side="left", padx=(0, 5))

        # Add both health bar and label to support both base and GUI classes
        self.health_bar = ttk.Progressbar(
            health_frame, length=200, mode="determinate", maximum=100, value=100
        )
        self.health_bar.pack(side="left")

        # Add a health label as well
        self.health_label = tk.Label(
            health_frame, text="Health: 100", font=("Arial", 12), 
            bg="#34495e", fg="white"
        )
        self.health_label.pack(side="left", padx=5)

        # Score Section
        score_frame = tk.Frame(status_frame, bg="#34495e")
        score_frame.pack(side="right", padx=10)

        score_icon = tk.Label(
            score_frame, image=self.images["score_icon"], bg="#34495e"
        )
        score_icon.pack(side="left", padx=(0, 5))

        self.score_label = tk.Label(
            score_frame, text="Score: 0", font=("Arial", 12), bg="#34495e", fg="white"
        )
        self.score_label.pack(side="left")

    def create_game_area(self):
        # Game description text
        self.game_text = tk.Text(
            self.master,
            height=8,
            width=80,
            font=("Courier", 10),
            bg="#ecf0f1",
            wrap=tk.WORD,
        )
        self.game_text.pack(pady=10)

    def create_action_buttons(self):
        # Action Button Frame
        action_frame = tk.Frame(self.master, bg="#2c3e50")
        action_frame.pack(pady=10)

        # Define action game text.
        actions = [
            ("🌳 Explore Forest", self.explore_forest),
            ("🏖️ Search Beach", self.search_beach),
            ("⛰️ Climb Mountain", self.climb_mountain),
            ("😴 Rest", self.rest),
        ]

        # Create buttons
        for text, command in actions:
            btn = tk.Button(
                action_frame,
                text=text,
                command=command,
                bg="#3498db",
                fg="black",
                font=("Arial", 10),
            )
            btn.pack(side="left", padx=5)

    def create_inventory_display(self):
        # Inventory Frame
        inventory_frame = tk.Frame(self.master, bg="#2c3e50")
        inventory_frame.pack(pady=5)

        inventory_icon = tk.Label(
            inventory_frame, image=self.images["inventory_icon"], bg="#2c3e50"
        )
        inventory_icon.pack(side="left", padx=(0, 5))

        self.inventory_label = tk.Label(
            inventory_frame,
            text="Inventory: Empty",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="white",
        )
        self.inventory_label.pack(side="left")


if __name__ == "__main__":
    main()