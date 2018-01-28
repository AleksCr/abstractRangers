import random
import json
from race import Race


class Galaxy:
    def __init__(self):
        self.systems = []
        self.id = 200

    def init_gen(self):
        for i in range(60):
            ss = StarSys()
            ss.init_gen()
            self.systems.append(ss)

    def show_galaxy(self):
        for system in self.systems:
            print(system.name)
            for planet in system.planets:
                print("     "+planet.name)

    def dump_world(self):
        data={}
        for system in self.systems:
            data[system.name] = {}
            for planet in system.planets:
                data[system.name]["x"] = system.x
                data[system.name]["y"] = system.y
                data[system.name][planet.name] = planet.type
        with open('galaxy.json', 'w') as fp:
            json.dump(data, fp)
        print("")

    def galaxy2html(self, type):
        with open("map.html","w") as htmlfile:
            htmlfile.write("")
        if(type == "text"):
            with open("map.html","a") as htmlfile:
                for system in self.systems:
                    htmlfile.write(system.name+"<ul>")
                    # print(len(system.planets))
                    for planet in system.planets:
                        htmlfile.write("<li>" + planet.name + " - " + planet.type + "</li>")
                    htmlfile.write("</ul>")
        elif(type == "graph"):
            with open("map.html", "a") as htmlfile:
                for system in self.systems:
                    color = "white"
                    if system.planets:
                        for planet in system.planets:
                            if(planet.owner != None):
                                color = planet.owner().color
                    htmlfile.write("<body bgcolor = \"black\">")
                    htmlfile.write("<img src=\"images/star.png\" style=\"position: absolute; top: "+str(system.x)+"px; left: "+str(system.y)+"px\">")
                    htmlfile.write("<span  style=\"position: absolute; color: "+str(color)+"; top: "+str(system.x+20)+"px; left: "+str(system.y-15)+"px\">"+system.name+"</span>")


class StarSys:
    def __init__(self):
        self.id = 1
        self.name = "star"
        self.x=random.randint(100, 800)
        self.y=random.randint(0, 800)
        self.planets = []

    def init_gen(self):
        names_one = ["Ar", "Ma", "Da", "Kun", "Tor", "Vol", "She", "Tu", "He", "Vit"]
        names_other = ["moon", "he", "mouse", "sity", "lol", "gor", "san", "dol", "shtein"]
        self.name = random.choice(names_one) + random.choice(names_other)
        for i in range(random.randint(0, 9)):
            pl = Planet()
            pl.init_gen()
            self.planets.append(pl)


class Planet:
    def __init__(self):
        self.type = random.choice(["Barren rock","Gas giant","Earthlike","Oceanic","Metan world"])
        self.owner = None
    name = "planet"

    def init_gen(self):
        names_one = ["Ka", "La", "Nas", "Ver", "Mi", "God", "Am", "Ev", "Do", "Too"]
        names_other = ["kol", "nas", "vor", "taun", "tor", "rog", "en", "imic", "pain"]
        self.name = random.choice(names_one) + random.choice(names_other)


# gal = Galaxy()
# gal.init_gen()
# gal.dump_world()
# gal.show_galaxy()
# gal.galaxy2html("text")
# gal.galaxy2html("graph")