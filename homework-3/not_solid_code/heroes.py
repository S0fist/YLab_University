from antagonistfinder import AntagonistFinder
from abc import ABC, abstractmethod


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        pass

    def ultimate(self):
        pass


class Gunner(SuperHero, ABC):
    @abstractmethod
    def fire_a_gun(self):
        pass


class Melee(SuperHero, ABC):
    @abstractmethod
    def roundhouse_kick(self):
        pass


class ChackNoris(Gunner, SuperHero):
    def __init__(self):
        super(ChackNoris, self).__init__('Chack Norris', False)

    def attack(self):
        self.fire_a_gun()

    def fire_a_gun(self):
        print("PIU PAF")


class Superman(Melee, SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        self.roundhouse_kick()

    def roundhouse_kick(self):
        print('Bump')

    def ultimate(self):
        self.incinerate_with_lasers()

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')
