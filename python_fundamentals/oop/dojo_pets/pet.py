class Pet:
    def __init__( self, name , pet_type , tricks ):
        self.name = name
        self.pet_type = pet_type
        self.tricks = tricks
        self.energy = 100
        self.health = 100

    # implement the following methods:
    def sleep(self):
        print(f"{self.name} falls asleep. They have good dreams.")# - increases the pets energy by 25
        if self.energy < 75:
            self.energy += 25
            print(f"{self.name} recovers 25 energy! Energy: {self.energy}.")
        else:
            self.energy = 100
            print(f"{self.name}'s energy is maxed!")

    def eat(self):
        print(f"{self.name} eats yummy food. They have a full tummy.") # - increases the pet's energy by 5 & health by 10
        if self.energy < 95:
            self.energy += 5
            print(f"{self.name} recovers 5 energy! Energy: {self.energy}.")
        else:
            self.energy = 100
            print(f"{self.name}'s health is maxed!")

        if self.health < 90:
            self.health += 10
            print(f"{self.name} recovers 5 health! Health: {self.health}.")
        else:
            self.health = 100
            print(f"{self.name}'s health is maxed!")

    def play(self):
        if self.health > 0 or self.energy > 0:
            print(f"{self.name} plays! They bonk on things and roll around.")# - decreases the pet's health by 5 decreases energy by 15
            if self.health > 5:
                self.health -= 5
                print(f"{self.name} drops 5 health! Health: {self.health}.")
            else:
                self.health = 0
                print(f"{self.name}'s health is depleted! Give them a break!")

            if self.energy > 15:
                self.energy -= 15
                print(f"{self.name} recovers 15 energy! Energy: {self.energy}.")
            else:
                self.energy = 0
                print(f"{self.name}'s health is depleted! Give them a break!")

        else:
            print(f"{self.name}'s is tired! Give them a break! Energy: {self.energy}. Health: {self.health}.")


    def noise(self):
        if self.energy > 0:
            print(f"{self.name} makes a cute noise! They are very energetic.")# - prints out the pet's sound decreases energy by 5
            if self.energy > 5:
                self.energy -= 5
                print(f"{self.name} drops 5 health! Health: {self.energy}.")
            else:
                self.energy = 0
                print(f"{self.name}'s health is depleted! Give them a break!")
        else:
            print(f"{self.name}'s health is depleted! Give them a break!")
