class GameObject:

    # Initializing the fields of the class
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    # Implementing the methods of our class
    def look(self):
        # We're formatting the string so it shows the name and appearance of the object
        return f"You look at the {self.name}. {self.appearance}\n"

    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"

    def sniff(self):
        return f"You sniff the {self.name}. {self.smell}\n"


# Creating a game object that instantiates our GameObject class
game_object = GameObject("Knife", "Some appearance", "Some feel", "Some smell")

# We can access an object's fields to modify them
game_object.name = "Spoon"
# And call out for its methods as seen below
print(game_object.sniff())