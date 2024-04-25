class GameObject:

    # Sets up an instance of GameObject with name, appearance, feel, and smell
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    # Returns string describing object appearance
    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"

    # Returns string describing object feel
    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"

    # Returns string describing object smell
    def sniff(self):
        return f"You sniff the {self.name}. {self.smell}\n"


class Room:
    # Our Room class has an escape code and a list of game objects as attributes/fields
    escape_code = 0
    game_objects = []

    # Initializer
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    # Returns whether the code of the room matches the code entered by the player
    def check_code(self, code):
        return self.escape_code == code

    # Returns a list with all the names of the objects we have in our room
    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names
        