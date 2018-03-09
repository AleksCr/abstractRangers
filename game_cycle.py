import galaxy
import race
import turn
import ship
import fabrication


# gal = galaxy.Galaxy()
galaxy.gal.init_gen()

game_exit = 0

while game_exit != 1 :
    galaxy.gal.galaxy2html("graph")
    action = input("input command: ")
    if action == "makeciv":
        race.Race(galaxy.gal)
    elif action == "turn" or action == "t":
        turn.gala_time.time_turn()
    elif action == "cheatship":
        has_ai = input("0 if no ai, anything else if it is: ")
        sys = None
        for system in galaxy.gal.systems:
            if system.planets:
                for planet in system.planets:
                    if planet.owner != None:
                        sys = system
                        break
        if sys is None:
            continue
        new_ship = ship.Ship(sys)
        if has_ai:
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
        for system in galaxy.gal.systems:
            for search_ship in system.ships:
                if search_ship.id == int(sh):
                    print("success! ship id is " + str(search_ship.id) + ". Ship located in " + system.name + " system")
                    new_sys = input("Enter new location system name: ")
                    break
        manage_ship = search_ship
        for system in galaxy.gal.systems:
            if system.name == new_sys:
                manage_ship.new_location(system)
                print("Hyper jump! New ship loc is " + system.name + " system!")
                break
    elif action == "shipcount":
        i = 0
        for system in galaxy.gal.systems:
            for search_ship in system.ships:
                i = i + 1
        print(i)
    elif action == "debug":
        inp = input("input debug command: ")
        if inp == "ship_ai":
            print("ship")
        elif inp == "race_ai":
            print("race")
        elif inp == "fab":
            for system in galaxy.gal.systems:
                if system.planets:
                    for planet in system.planets:
                        if planet.owner != None:
                            sys = system
                            break
            if sys is None:
                continue
            fabrication.Fabricate(sys, ship.Frigate)

