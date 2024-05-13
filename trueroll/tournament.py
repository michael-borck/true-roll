from typing import List, Dict
from game import Game
from bowler import Bowler
from alley import Alley

class Tournament:
    def __init__(self, bowlers: List[Bowler], alley: Alley, num_games: int = 1):
        """
        Initializes a tournament with a set of bowlers, the venue of the tournament, and the number of games each bowler will play.
        
        :param bowlers: A list of `Bowler` objects representing the participants.
        :param alley: The `Alley` object where the tournament takes place.
        :param num_games: The number of games each bowler will play in the tournament.
        """
        self.bowlers = bowlers
        self.alley = alley
        self.num_games = num_games
        self.results = {bowler.name: [] for bowler in bowlers}

    def run_tournament(self):
        """
        Simulate the entire tournament, running the specified number of games for each bowler.
        """
        for _ in range(self.num_games):
            game = Game(self.bowlers, self.alley)
            game_results = game.simulate_game()
            for name, scores in game_results.items():
                self.results[name].append(scores)

    def get_results(self) -> Dict[str, List[int]]:
        """
        Calculate and return the total scores for each bowler over the course of the tournament.
        
        :return: A dictionary with bowler names as keys and lists of their scores as values.
        """
        total_scores = {name: [sum(sum(frame) for frame in game) for game in games] for name, games in self.results.items()}
        return total_scores

    def get_average_scores(self) -> Dict[str, float]:
        """
        Calculate and return the average scores for each bowler in the tournament.
        
        :return: A dictionary with bowler names as keys and their average score as values.
        """
        average_scores = {name: sum(scores) / len(scores) if scores else 0 for name, scores in self.get_results().items()}
        return average_scores
