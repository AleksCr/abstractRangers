import random
# from galaxy import Galaxy, StarSys
import galaxy


class Race:
    def __init__(self):
        self.money = random.randint(100, 800)
        self.color = "green"

    def create_civ(self, gal):
        gal_planets = []
        for system in gal.systems:
            if system.planets:
                for planet in system.planets:
                    gal_planets.append(planet)
        rand_planet = random.choice(gal_planets)
        # for system in gal.systems:
        #     print(system.name)
        rand_planet.owner = self

    def return_color(self):
        return self.color