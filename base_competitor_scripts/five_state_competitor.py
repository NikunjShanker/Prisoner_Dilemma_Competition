from competition import Competitor
import random

class FiveStateCompetitor(Competitor):
    def select_play(self):
        """
        Chooses random move in the first round then chooses move based on five states. The lower two states result
        in cooperation and the upper two states result in aggression. If the middle state is chosen, the move is 
        chosen at random. The state updates based on the opponent's previously played move.
        """
        
        round_num = self.competition.round_num
        opp_plays = self.competition.plays[self.opp_num]
        favor = 0

        if round_num == 0:
            return random.randint(0, 1)
        
        favor += opp_plays[-1] * 2 - 1
        
        if favor > 2:
            favor = 2
        elif favor < -2:
            favor = -2

        if favor > 0:
            return 1
        elif favor < 0:
            return 0

        return random.randint(0, 1)

    def __str__(self):
        return "five_state"
    