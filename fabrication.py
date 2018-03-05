import ship


class Fabricate:
    def __init__(self, place, obj):
        print(obj.fab_points)
        # sh = ship.Ship(place)
        sh = obj(place)
        class_name = type(sh).__name__
        print(class_name)

