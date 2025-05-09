import os
import importlib
import inspect
from pathlib import Path

str_break = "=" * 128

class Competition:
    def __init__(self, competitors):
        self.competitiors = competitors
        self.match_num = 1
        self.match_queue = []
        self.scores = {}

        # Temp lists to be emptied at start of each match
        self.first_plays = []
        self.second_plays = []
        self.plays = [self.first_plays, self.second_plays]
        self.round_winners = []
        # Temp int to be reset at start of each match
        self.round_num = 0

    def play_competition(self):
        # Create queue of matches
        for i in range(len(self.competitiors)):
            for j in range(i + 1, len(self.competitiors)):
                a = self.competitiors[i]
                b = self.competitiors[j]

                self.match_queue.append((a, b))
                self.scores[a] = 0
                self.scores[b] = 0
        
        # Output the intro
        self.output_intro()

        # Play each match
        for match in self.match_queue:
            self.play_match(match[0], match[1])
            self.match_num += 1

        # Output final scores and standings
        self.output_results()
    
    def play_match(self, first_comp, second_comp):
        # Reset the plays lists
        self.first_plays = []
        self.second_plays = []
        self.round_winners = []
        self.round_num = 0
        f_points = 0
        s_points = 0

        # Inform the competitors of their assigned number
        first_comp.set_num(0)
        second_comp.set_num(1)
        
        while(self.round_num < 10):
            first_play = first_comp.select_play()
            second_play = second_comp.select_play()
            self.first_plays.append(first_play)
            self.second_plays.append(second_play)
            self.plays = [self.first_plays, self.second_plays]

            if first_play == 1:
                if second_play == 0:
                    f_points += 2
                    self.round_winners.append(0)
                else:
                    self.round_winners.append(-1)
            else:
                if second_play == 1:
                    s_points += 2
                    self.round_winners.append(1)
                else:
                    f_points += 1
                    s_points += 1
                    self.round_winners.append(2)

            self.round_num += 1

        self.scores[first_comp] += f_points
        self.scores[second_comp] += s_points
        winner = 1
        if f_points < s_points:
            winner = 2
        elif f_points == s_points:
            winner = 0
        self.output_match(first_comp, second_comp, winner)

    def output_intro(self):
        print("\n\n")
        print(str_break)
        print(f"The competition has {len(self.competitiors)} competitors:")
        print(str_break)

        for competitor in self.competitiors:
            print(competitor, end="\n")

        print("\n\n")

    def output_match(self, first_comp, second_comp, winner):
        # Calculate different in competitor names
        first_name = str(first_comp)
        second_name = str(second_comp)
        results_name = "results"
        diff = len(first_name) - len(second_name)
        if diff < 0:
            first_name += " " * -diff
            results_name += " " * (len(second_name) - len(results_name))
        else:
            second_name += " " * diff
            results_name += " " * (len(first_name) - len(results_name))

        # Translate plays and results to strings
        first_plays_str = ""
        second_plays_str = ""
        results_str = ""
        for (f_play, s_play) in zip(self.first_plays, self.second_plays):
            first_plays_str += str(f_play)
            second_plays_str += str(s_play)

            result = "."
            if f_play == 1:
                if s_play == 0:
                    result = "A"
            else:
                if s_play == 1:
                    result = "B"
                else:
                    result = "+"
            results_str += result

        # Add the win tags to the result strings
        if winner == 1:
            first_plays_str += " (winner)"
        elif winner == 2:
            second_plays_str += " (winner)"
        else:
            first_plays_str += " (tie)"
            second_plays_str += " (tie)"

        # Output the results of the match
        print(f"MATCH {self.match_num} ({first_name.strip()} VS {second_name.strip()})")
        print(str_break)
        print(f"Player A: {first_name} | ", end="")
        print(f"{first_plays_str}")
        print(f"Player B: {second_name} | ", end="")
        print(f"{second_plays_str}")
        results_brk = " " * 12
        if diff == 0: results_brk = " " * 11
        print(f"{results_name}{results_brk} ", end="")
        print(f"{results_str}")
        print(str_break)
        print("\n")

    def output_results(self):
        print("\nFINAL RESULTS")
        print(str_break)
        
        standings = sorted(self.scores.items(), key=lambda item: item[1], reverse=True)
        counter = 1
        for placement in standings:
            if counter == 1:
                print("|| 1st Place ||", end=" ")
            elif counter == 2:
                print("|| 2nd Place ||", end=" ")
            elif counter == 3:
                print("|| 3rd Place ||", end=" ")
            counter += 1

            print(str(placement[0]), "-", placement[1], "points")

        print(str_break)
        print("\n\n")

 
class Competitor:
    def __init__(self):
        self.points = 0
        self.num = 0
        self.opp_num = 0
        self.competition = None

    def __str__(self):
        return "unnamed"

    def set_num(self, num):
        self.num = num
        self.opp_num = 1 - num

    def select_play(self):
        pass

    def add_points(self, point_total):
        self.points += point_total


def import_all_classes_from_folder(folder_name):
    folder_path = Path(folder_name)
    all_classes = {}

    for file in folder_path.glob("*.py"):
        if file.name == "__init__.py":
            continue
        module_name = f"{folder_name.replace('/', '.')}.{file.stem}"
        module = importlib.import_module(module_name)
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if obj.__module__ == module.__name__:
                all_classes[name] = obj
    return all_classes
    

if __name__ == "__main__":
    classes = import_all_classes_from_folder("competitor_scripts")
    competitors = [cls() for cls in classes.values()]
    competition = Competition(competitors)
    for competitor in competitors:
        competitor.competition = competition
    competition.play_competition()
