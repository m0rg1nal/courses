class Mammal:
    def __init__(self, name, species):
        self._name = name
        self._species = species

    def get_name(self):
        return self._name

    def get_species(self):
        return self._species


class Predator(Mammal):
    def __init__(self, name, species, prey):
        super().__init__(name, species)
        self._prey = prey

    def get_prey(self):
        return self._prey
