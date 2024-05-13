from typing import List, Tuple, Dict, Iterator
from bowler import Bowler
from alley import Alley

class Game:
    def __init__(self, bowlers: List[Bowler], alley: Alley):
        """
        Initialize a game with a list of bowlers and the alley where the game is played.
        
        :param bowlers: List of Bowler objects participating in the game.
        :param alley: The Alley object specifying the lane type and oil pattern.
        """
        self.bowlers = bowlers
        self.alley = alley

    def simulate_frame(self, bowler: Bowler, frame_number: int) -> Tuple[int, ...]:
        """
        Simulate a single frame for a given bowler based on the frame number.
        
        :param bowler: The Bowler object for whom the frame is simulated.
        :param frame_number: The frame number (0-indexed, 0-9).
        :return: A tuple representing the result of the frame (pins knocked down in each roll).
        """
        if frame_number < 9:
            return self.simulate_regular_frame(bowler)
        else:
            return self.simulate_last_frame(bowler)

    def simulate_regular_frame(self, bowler: Bowler) -> Tuple[int, int]:
        """
        Simulate a regular frame (not the last one), accounting for strikes and open frames.
        
        :param bowler: The Bowler object for whom the frame is simulated.
        :return: A tuple of two integers representing the pins knocked down in each roll.
        """
        # Example simulation logic, replace with actual simulation logic.
        return (10, 0) if np.random.rand() < bowler.strike_prob else (5, 4)  # Example data.

    def simulate_last_frame(self, bowler: Bowler) -> Tuple[int, int, int]:
        """
        Simulate the 10th frame, which may include up to three rolls depending on the bowler's performance.
        
        :param bowler: The Bowler object for whom the last frame is simulated.
        :return: A tuple of up to three integers representing the pins knocked down in each roll.
        """
        # Example simulation logic for the last frame.
        return (10, 10, 10)  # Example data.

    def frame_by_frame_generator(self) -> Iterator[Dict[str, Tuple[int, ...]]]:
        """
        A generator to simulate the game frame-by-frame, yielding results for each frame for all bowlers.
        
        :return: An iterator that yields a dictionary representing the frame results of each bowler.
        """
        for frame_number in range(10):
            frame_results = {}
            for bowler in self.bowlers:
                frame_results[bowler.name] = self.simulate_frame(bowler, frame_number)
            yield frame_results

    def simulate_game(self) -> Dict[str, List[Tuple[int, ...]]]:
        """
        Simulate a complete game for all bowlers, returning the frame-by-frame results.
        
        :return: A dictionary where keys are bowler names and values are lists of tuples, each tuple representing a frame.
        """
        results = {bowler.name: [] for bowler in self.bowlers}
        for frame_results in self.frame_by_frame_generator():
            for name, frame in frame_results.items():
                results[name].append(frame)
        return results
