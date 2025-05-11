from competition import Competitor

class OptimisticCompetitor(Competitor):
    def select_play(self):
        """
        Always chooses cooperation.
        """
        
        return 0

    def __str__(self):
        return "optimistic"
    