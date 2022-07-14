from heroes import Superman, SuperHero, ChackNoris
from places import Kostroma, Tokyo, Earth, Mars, MediaTV


def save_the_place(hero: SuperHero, Place, planet):
    hero.find(Place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    MediaTV.create_news(Place, hero, planet)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), Earth())
    print('-' * 20)
    save_the_place(ChackNoris(), Tokyo(), Mars())
