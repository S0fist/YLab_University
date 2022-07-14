from abc import ABC, abstractmethod


class Place(ABC):
    @abstractmethod
    def find_trouble(self):
        print('Something is coming')


class Kostroma(Place):
    city_name = 'Kostroma'

    def find_trouble(self):
        print('Orcs hide in the forest')


class Tokyo(Place):
    city_name = 'Tokyo'

    def find_trouble(self):
        print('Godzilla stands near a skyscraper')


class Planet(ABC):
    @abstractmethod
    def announcment(self):
        print("Calling planets")


class Earth(Planet):
    coordinates = [159.34523153, 101.43526561123]

    def announcment(self):
        print("Earth if safe!")


class Mars(Planet):
    coordinates = [120.3645673153, 56.4532254121123]

    def announcment(self):
        print("Mars if safe!")


class MediaTV:

    def create_news(self, hero, planet):
        place_name = getattr(self, 'city_name')
        hero_name = getattr(hero, 'name')
        print(f'{hero_name} saved the {place_name}!')
        if isinstance(planet, Planet):
            planet.announcment()
