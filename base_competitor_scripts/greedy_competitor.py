from competition import Competitor

class GreedyCompetitor(Competitor):
    def select_play(self):
        """
        Always chooses aggression.
        """
        
        return 1

    def __str__(self):
        return "greedy"
    