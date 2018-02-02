from galaxy import Galaxy
from race import Race
import turn
import ship


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
        ship.Ship(sys)
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
            for seach_ship in system.ships:
                if seach_ship.id == int(sh):
                    print("success! ship id is " + str(seach_ship.id) + ". Ship located in " + system.name + " system")
                    new_sys = input("Enter new location system name: ")
                    break
        manage_ship = seach_ship
        for system in gal.systems:
            if system.name == new_sys:
                manage_ship.new_location(system)
                print("Hyper jump! New ship loc is " + manage_ship.system.name + " system!")
    elif action == "test":
        inp = input("num: ")
        if int(inp) == 1:
            print("kruto!")
    gal.galaxy2html("graph")

# Race.create_civ(Race, gal)
# gal.galaxy2html("graph")
