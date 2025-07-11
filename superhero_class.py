# Base class
class Character:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin
        self._power_level = 50  # protected attribute

    def display_info(self):
        print(f"{self.name} from {self.origin} has power level {self._power_level}")

# Subclass with inheritance + encapsulation
class Superhero(Character):
    def __init__(self, name, origin, superpower):
        super().__init__(name, origin)
        self.superpower = superpower

    def upgrade_power(self, amount):
        self._power_level += amount
        print(f"{self.name} upgraded! Power level is now {self._power_level}")

    def use_power(self):
        print(f"{self.name} uses {self.superpower}!")

# Creating objects
hero1 = Superhero("StarFlash", "Nebula-X", "Light Speed")
hero2 = Superhero("AquaQueen", "Atlantis", "Water Control")

hero1.display_info()
hero1.use_power()
hero1.upgrade_power(30)