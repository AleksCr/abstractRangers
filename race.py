import random
import ai_race

global_race_id = 1

race_colors = ["red", "yellow", "green", "pink", "blue"]
race_container = []


class Race:
    def __init__(self, gal):
        global global_race_id, race_colors
        if not race_colors:
            del self
            return
        self.money = random.randint(100, 800)
        self.id = global_race_id

        global_race_id += 1
        gal_planets = []
        system = random.choice(gal.systems)
        if system.planets:
            planet = random.choice(system.planets)
            if(planet.owner != None):
                print("There is owner already! Delete Race..")
                del self
                return
            gal_planets.append(planet)
        self.color = random.choice(race_colors)
        race_colors.remove(self.color)
        rand_planet = random.choice(gal_planets)
        rand_planet.owner = self
        race_container.append(self)
        ai_obj = ai_race.AI_Race(self)

    def make_money(self):
        self.money += random.randint(1,100)

    def manufacture(self, obj):
        return 0

    def return_color(self):
        return self.color
