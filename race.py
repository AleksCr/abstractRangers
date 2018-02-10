import random
# from galaxy import Galaxy, StarSys
import galaxy
import ai_race

global_race_id = 1


class Race:
    def __init__(self, gal):
        global global_race_id
        self.money = random.randint(100, 800)
        self.color = "green"
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
        print("test")
        rand_planet.owner = self
        print(str(rand_planet) + "" + str(rand_planet.owner))

    def make_money(self):
        self.money += random.randint(1,100)

    def manufacture(self, obj):
        return 0

    def return_color(self):
        return self.color