from competition import Competitor
import random, math

"""
Author's Note:
    This file must be named 'yournamehere.py'. Your class must be named 'yournamehereCompetitor' and must be a
    subclass of Competitor. Only the inherited select_play() and __str__() functions are allowed to be modified.
    You are welcome to add any new methods and variables as you see fit. No additional imports are allowed. 
    Adding comments is optional but heavily encouraged. You are encouraged to look through the
    'base_competitor_scripts' folder to gain inspiration and mimic their algorithm structure.
"""

# TODO: Rename this file and this class.
class SampleCompetitor(Competitor):
    def select_play(self):
        round_num = self.competition.round_num              # The number of the current round (ranges from 0 to 9).
        my_plays = self.competition.plays[self.num]         # An ordered list of all of your previous moves.
        opp_plays = self.competition.plays[self.opp_num]    # An ordered list of all of your opponent's previous moves.
        round_winners = self.competition.round_winners      # An ordered list of all win states in the previous rounds.
        """
        round_winners[i] = self.num means that you won the i-th round
        round_winners[i] = self.opp_num means that your opponent won the i-th round
        round_winners[i] = -1 means that neither you nor your opponent won the i-th round
        round_winners[i] = 2 means that both you and your opponent won the i-th round
        """

        # TODO: Put your algorithm implementation here. This function must return either a 0 or 1.
        pass

    def __str__(self):
        # TODO: Rename this returned string.
        return "yournamehere"
    