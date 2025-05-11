from competition import Competitor
import random

class RandomCompetitor(Competitor):
    def select_play(self):
        """
        Always chooses the move randomly.
        """
        
        return random.randint(0,1)

    def __str__(self):
        return "random"
    