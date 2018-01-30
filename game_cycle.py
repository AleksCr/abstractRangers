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
    gal.galaxy2html("graph")

# Race.create_civ(Race, gal)
# gal.galaxy2html("graph")
