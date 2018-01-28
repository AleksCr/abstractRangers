from galaxy import Galaxy
from race import Race
gal = Galaxy()
gal.init_gen()


Race.create_civ(Race, gal)
gal.galaxy2html("graph")
