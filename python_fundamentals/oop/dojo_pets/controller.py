from ninja import Ninja
from pet import Pet
from dog import Dog
from cat import Cat

nine_tails = Pet("Nine Tails", "Fox", "Foxfire")
leia = Dog("Leia", "Mix", "Sit")
tumbles = Cat("Tumbles", "God", "Rule the World")
naruto = Ninja("Naruto", "Uzumaki", "Pet Ramen", "Number 1 Kibble", tumbles)



naruto.walk()
naruto.feed()
naruto.bathe()
# nine_tails.eat()
# nine_tails.play()
# nine_tails.noise()
# nine_tails.sleep()