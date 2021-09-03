from pet import Pet
class Dog(Pet):
    def __init__(self, name, pet_type, tricks):
        super().__init__(name, pet_type, tricks)
        self.energy = 125
        self.health = 95
    
    def noise(self):
        if self.energy > 0:
            print(f"{self.name} makes a bork bork! They are very energetic.")# - prints out the pet's sound decreases energy by 5
            if self.energy > 5:
                self.energy -= 5
                print(f"{self.name} drops 5 health! Health: {self.energy}.")
            else:
                self.energy = 0
                print(f"{self.name}'s health is depleted! Give them a break!")
        else:
            print(f"{self.name}'s health is depleted! Give them a break!")
