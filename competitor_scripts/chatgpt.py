from competition import Competitor

class ChatGPTCompetitor(Competitor):
    def select_play(self):
        """
        Cooperative for the first three rounds, then in the following order:
            - Aggressive if the opponent is aggressive
            - Aggressive if the opponent is mostly aggressive with a 25% chance of being forgiving
            - Aggressive if the opponent was just previously aggressive with a 25% chance of being forgiving
        """

        round_num = self.competition.round_num
        opp_plays = self.competition.plays[self.opp_num]

        if round_num < 3:
            return 0
        
        opp_defections = sum(opp_plays)

        if opp_plays[-3:] == [1, 1, 1]:
            return 1
        
        if opp_defections > round_num / 2:
            if round_num % 4 == 0:
                return 0
            else:
                return 1
            
        if opp_plays[-1] == 1:
            if round_num % 4 != 0:
                return 1

        return 0

    def __str__(self):
        return "chatgpt"
    