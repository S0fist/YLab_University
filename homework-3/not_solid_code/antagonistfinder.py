from places import Place


class AntagonistFinder:

    def get_antagonist(self, place):
        if isinstance(place, Place):
            place.find_trouble()
