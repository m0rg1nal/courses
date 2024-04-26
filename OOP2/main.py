from mammals import Mammal, Predator

lion = Predator("Bob", "Lion", "Antelope")
human = Mammal("John", "Human")

print(lion.get_name())
print(lion.get_species())
print(lion.get_prey())

print(human.get_name())
print(human.get_species())