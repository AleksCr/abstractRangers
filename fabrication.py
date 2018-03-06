class Fabricate:
    def __init__(self, place, obj):
        print(obj.fab_points)
        sh = obj(place)
        # print(type(sh).__name__)

