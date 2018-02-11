import random
# from galaxy import Galaxy, StarSys
import galaxy
import ai_race

global_race_id = 1

race_colors = ["red","yellow","green","pink","blue"]

class Race:
    def __init__(self, gal):
        global global_race_id, race_colors
        if not race_colors:
            del self
            return
        self.money = random.randint(100, 800)
        self.color = random.choice(race_colors)
        race_colors.remove(self.color)
        self.id = global_race_id

        global_race_id += 1
        gal_planets = []
        for system in gal.systems:
            if system.planets:
                for planet in system.planets:
                    gal_planets.append(planet)
        rand_planet = random.choice(gal_planets)
        # for system in gal.systems:
        #     print(system.name)
        rand_planet.owner = self

    def make_money(self):
        self.money += random.randint(1,100)

    def manufacture(self, obj):
        return 0

    def return_color(self):
        return self.color