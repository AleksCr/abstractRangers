import random
import galaxy


class AI_Ship:
    def __init__(self, owner_ship):
        self.ai_owner = owner_ship

    def ai_cycle(self):
        print("ship ai cycle...")
        #print(random.__file__)
        sys = random.choice(galaxy.gal.systems)
        print("ai jump point == "+sys.name)
        self.ai_owner.new_location(sys) # ToDO: ограничить кораблю количество прыжков за ход