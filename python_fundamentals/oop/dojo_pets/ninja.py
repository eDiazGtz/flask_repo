from pet import Pet

class Ninja:
    def __init__( self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    # implement the following methods:
    def walk(self): # - walks the ninja's pet invoking the pet play() method
        print(f"{self.first_name} walks {self.pet.name}. You have a great time and play together!")
        self.pet.play()
        

    def feed(self): # - feeds the ninja's pet invoking the pet eat() method
        print(f"{self.first_name} feeds {self.pet.name}. They like the food very much!")
        self.pet.eat()

    def bathe(self): # - cleans the ninja's pet invoking the pet noise() method
        print(f"{self.first_name} bathes {self.pet.name}. They're not sure how they feel about it and make some noise")
        self.pet.noise()