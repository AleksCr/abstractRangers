import random
import json
from race import Race
import turn


class Galaxy:
    def __init__(self):
        self.systems = []
        self.id = 200

    def init_gen(self):
        for i in range(1):
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
                    for planet in system.planets:
                        htmlfile.write("<li>" + planet.name + " - " + planet.type + "</li>")
                    htmlfile.write("</ul>")
        elif(type == "graph"):
            with open("map.html", "a") as htmlfile:
                htmlfile.write("<body bgcolor = \"black\">")
                htmlfile.write("<p><span style=\"position: absolute; color: white\">Galaxy time: "+turn.gala_time.get_str_time()+"</span></p>")
                count_races = 0
                for system in self.systems:
                    color = "white"
                    if system.planets:
                        for planet in system.planets:
                            if(planet.owner != None):
                                count_races += 1
                                color = planet.owner.color
                                print(str(count_races))
                    #             ToDo: Замутить функцию красящую систему, населенную несколькими расами
                    htmlfile.write("<img src=\"images/star_" + system.type + ".png\" style=\"position: absolute; top: "+str(system.x)+"px; left: "+str(system.y)+"px\">")
                    if count_races <= 1:
                        htmlfile.write("<span  style=\"position: absolute; color: "+str(color)+"; top: "+str(system.x+20)+"px; left: "+str(system.y-15)+"px\">"+system.name+"</span>")
                    else:
                        htmlfile.write("<span  style=\"position: absolute; color: " + " lime" + "; top: " + str(
                            system.x + 20) + "px; left: " + str(system.y - 15) + "px\">" + system.name + "</span>")
                    if system.ships:
                        htmlfile.write("<img src=\"images/gala_ship.png\" style=\"position: absolute; top: " + str(system.x-10) + "px; left: " + str(system.y+10) + "px\">")


class StarSys:
    def __init__(self):
        self.id = 1
        self.name = "star"
        self.x=random.randint(100, 800)
        self.y=random.randint(0, 800)
        self.planets = []
        self.ships = []
        self.type = random.choice(["red","orange","blue","yellow"])

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


