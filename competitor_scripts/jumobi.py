from competition import Competitor
import random

class JumobiCompetitor(Competitor):
    def select_play(self):
        """
        Cooperative for the first round, copycat for the next four, and then strictly aggressive.
        """
        
        round_num = self.competition.round_num
        opp_plays = self.competition.plays[self.opp_num]

        if round_num == 0:
            return 0
        
        if round_num < 5:
            return opp_plays[-1]

        return 1

    def __str__(self):
        return "jumobi"
    