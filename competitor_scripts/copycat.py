from competition import Competitor
import random

class CopycatCompetitor(Competitor):
    def select_play(self):
        """
        Random move for the first round then copies the move that the oppoonent played in the previous round.
        """
        
        round_num = self.competition.round_num
        opp_plays = self.competition.plays[self.opp_num]

        if round_num == 0:
            return random.randint(0, 1)
        
        return opp_plays[-1]

    def __str__(self):
        return "copycat"
    