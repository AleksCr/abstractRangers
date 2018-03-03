class Galaxy_time:
    def __init__(self):
        self.month = 1
        self.year = 3000

    def time_turn(self):
        if self.month < 12:
            self.month += 1
        else:
            self.year += 1
            self.month = 1

    def get_str_time(self):
        return str(self.month)+"."+str(self.year)


gala_time = Galaxy_time()
