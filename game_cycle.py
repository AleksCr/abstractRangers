from galaxy import Galaxy
from race import Race
import turn
import ship
import ai_race
import ai_ship


gal = Galaxy()
gal.init_gen()

game_exit = 0

while game_exit != 1 :
    action = input("input command: ")
    if action == "makeciv":
        Race.create_civ(Race, gal)
    elif action == "turn" or action == "t":
        turn.gala_time.time_turn()
    elif action == "cheatship":
        for system in gal.systems:
            if system.planets:
                for planet in system.planets:
                    if (planet.owner != None):
                        sys = system
                        break
        new_ship = ship.Ship(sys)
        new_ship.ai = 0
    elif action == "ship_info":
        info = input("id")
        print(info)
    elif action == "multiturn":
        turns = input("input num of turns: ")
        for i in range(int(turns)):
            turn.gala_time.time_turn()
        print(str(i)+" turns passed")
    elif action == "manage ship":
        sh = input("input ship id: ")
        for system in gal.systems:
            for search_ship in system.ships:
                if search_ship.id == int(sh):
                    print("success! ship id is " + str(search_ship.id) + ". Ship located in " + system.name + " system")
                    new_sys = input("Enter new location system name: ")
                    break
        manage_ship = search_ship
        for system in gal.systems:
            if system.name == new_sys:
                manage_ship.new_location(system)
                print("Hyper jump! New ship loc is " + system.name + " system!")
                break
    elif action == "shipcount":
        i = 0
        for system in gal.systems:
            for search_ship in system.ships:
                i=i+1
        print(i)
    elif action == "test":
        inp = input("num: ")
        if int(inp) == 1:
            print("kruto!")
    gal.galaxy2html("graph")

# Race.create_civ(Race, gal)
# gal.galaxy2html("graph")
