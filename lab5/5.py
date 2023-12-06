class Animal:
    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat

    def description(self):
        return f"This is a {self.species}. It lives in {self.habitat}."


class Mammal(Animal):
    def __init__(self, species, habitat, sound, legs):
        super().__init__(species, habitat)
        self.sound = sound
        self.legs = legs

    def make_sound(self):
        return f"The {self.species} makes the sound: {self.sound}"

    def movement(self):
        return f"{self.species} moves on {self.legs} legs."


class Bird(Animal):
    def __init__(self, species, habitat, wingspan, can_fly):
        super().__init__(species, habitat)
        self.wingspan = wingspan
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            return f"The {self.species} can fly with a wingspan of {self.wingspan} inches."
        else:
            return f"The {self.species} has wings but cannot fly."


class Fish(Animal):
    def __init__(self, species, habitat, size, deep_sea):
        super().__init__(species, habitat)
        self.size = size
        self.deep_sea = deep_sea

    def underwater_ability(self):
        if self.deep_sea:
            return f"The {self.species} is {self.size} inches and is found mostly in the deeper parts of the sea."
        else:
            return f"The {self.species} is {self.size} inches and is found mostly in more shallow water."

lion = Mammal("Lion", "Savannah", "Roar", 4)
eagle = Bird("Eagle", "Mountains", 72, True)
shark = Fish("Shark", "Oceans", 120, True)

# Call methods for each instance
print(lion.description())
print(lion.make_sound())
print(lion.movement())

print(eagle.description())
print(eagle.fly())

print(shark.description())
print(shark.underwater_ability())

