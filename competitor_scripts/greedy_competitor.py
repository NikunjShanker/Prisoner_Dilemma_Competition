from competition import Competitor

class GreedyCompetitor(Competitor):
    def select_play(self):
        return 1

    def __str__(self):
        return "greedy"
    