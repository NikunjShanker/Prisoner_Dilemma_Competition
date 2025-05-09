from competition import Competitor

class ProbabilityCompetitor(Competitor):
    def select_play(self):
        round_num = self.competition.round_num
        my_plays = self.competition.plays[self.num]
        opp_plays = self.competition.plays[self.opp_num]
        round_winners = self.competition.round_winners

        if round_num < 4:
            return round_num // 2

        split_favor = 0
        steal_favor = 0

        for i in range(round_num - 1):
            play = my_plays[i]
            round_winner = round_winners[i]
            if play == 0:
                if round_winner == 2:
                    split_favor += 1
            elif play == 1:
                if round_winner == self.num:
                    steal_favor += 1

        if split_favor > steal_favor:
            return 0
        return 1

    def __str__(self):
        return "probability"
    