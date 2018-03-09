# import game_cycle
import fabrication
import ship


class AI_Race:
    def __init__(self, race):
        ai_owner = race

    def ai_cycle(self):
        for system in gal.systems:
            if system.planets:
                for planet in system.planets:
                    if planet.owner != None:
                        sys = system
                        break
        fabrication.Fabricate(sys, ship.Frigate)