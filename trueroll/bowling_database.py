import sqlite3
from typing import List, Dict, Any

class BowlingDatabase:
    """Handles the storage and retrieval of bowling simulation data in an SQLite database.

    This class provides methods to add and manage bowlers, alleys, games, and detailed game statistics.
    """

    def __init__(self, db_name: str = 'bowling.db'):
        """
        Initializes the database connection and creates tables if they do not already exist.

        :param db_name: The filename of the database. Defaults to 'bowling.db'.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_tables()

    def create_tables(self):
        """Creates tables in the database if they do not exist to store bowlers, alleys, games, and game details."""
        c = self.conn.cursor()
        # Create tables for bowlers, alleys, oil patterns, games, and game details
        # ...

    def add_bowler(self, bowler: 'Bowler') -> int:
        """
        Adds a new bowler to the database or updates an existing bowler with the same name.

        :param bowler: An instance of the Bowler class containing bowler data.
        :return: The database ID of the added or updated bowler.
        """
        c = self.conn.cursor()
        c.execute('''
            INSERT INTO Bowlers (Name, Handedness, Style)
            VALUES (?, ?, ?) ON CONFLICT(Name) DO UPDATE SET
            Handedness=excluded.Handedness, Style=excluded.Style
        ''', (bowler.name, bowler.handedness, bowler.style))
        self.conn.commit()
        return c.lastrowid

    def add_alley(self, alley: 'Alley') -> int:
        """
        Adds a new bowling alley to the database.

        :param alley: An instance of the Alley class containing alley data.
        :return: The database ID of the added alley.
        """
        c = self.conn.cursor()
        c.execute('INSERT INTO Alleys (Name, Location, LaneType) VALUES (?, ?, ?)', 
                  (alley.name, alley.location, alley.lane_type))
        self.conn.commit()
        return c.lastrowid

    def add_game(self, date: str, alley_id: int, oil_pattern_id: int, frames: List[tuple]):
        """
        Adds a new game along with detailed frame data to the database.

        :param date: The date the game was played.
        :param alley_id: The database ID of the alley where the game was played.
        :param oil_pattern_id: The database ID of the oil pattern used in the game.
        :param frames: A list of tuples representing the frames played in the game.
        """
        c = self.conn.cursor()
        c.execute('INSERT INTO Games (Date, AlleyID, OilPatternID) VALUES (?, ?, ?)', (date, alley_id, oil_pattern_id))
        game_id = c.lastrowid
        total_score, strike_percentage, spare_percentage = self.calculate_stats(frames)
        c.execute('''
            INSERT INTO GameDetails (GameID, FrameData, TotalScore, StrikePercentage, SparePercentage)
            VALUES (?, ?, ?, ?, ?)
        ''', (game_id, str(frames), total_score, strike_percentage, spare_percentage))
        self.conn.commit()

    def calculate_stats(self, frames: List[tuple]) -> (int, float, float):
        """
        Calculate total score, strike, and spare percentages from frame data.

        :param frames: A list of tuples representing the frames played in the game.
        :return: A tuple containing the total score, strike percentage, and spare percentage.
        """
        total_score = 0  # Implement scoring calculation based on rules
        strikes = sum(1 for frame in frames if frame[0] == 10)
        spares = sum(1 for frame in frames if sum(frame[:2]) == 10 and frame[0] != 10)
        total_frames = len(frames)
        strike_percentage = (strikes / total_frames) * 100
        spare_percentage = (spares / total_frames) * 100
        return total_score, strike_percentage, spare_percentage

    def close(self):
        """Closes the database connection."""
        self.conn.close()
