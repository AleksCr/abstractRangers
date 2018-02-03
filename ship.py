global_ship_id = 1


class Ship:
    def __init__(self, system):
        global global_ship_id
        self.id = global_ship_id
        global_ship_id += 1
        self.ai = 1
        self.system = system
        system.ships.append(self)
        print("ship was created; id = " + str(self.id))
        print(self.return_location().name)

    def new_location(self, loc_system):
        if self in self.system.ships:
            self.system.ships.remove(self)
        self.system = loc_system
        loc_system.ships.append(self)

    def return_location(self):
        return self.system

    def turn_ai_off(self):
        self.ai = 0

