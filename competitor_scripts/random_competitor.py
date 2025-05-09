from competition import Competitor
import random

class RandomCompetitor(Competitor):
    def select_play(self):
        return random.randint(0,1)

    def __str__(self):
        return "random"
    