class Scoring:
    @staticmethod
    def traditional(frames: list) -> int:
        """
        Calculate the traditional bowling score from a list of frames.
        """
        score = 0
        rolls = []
        for frame in frames:
            rolls.extend(frame)

        for i in range(10):
            frame_index = i * 2
            if rolls[frame_index] == 10:  # Strike
                score += 10 + rolls[frame_index + 1] + rolls[frame_index + 2]
            elif rolls[frame_index] + rolls[frame_index + 1] == 10:  # Spare
                score += 10 + rolls[frame_index + 2]
            else:
                score += rolls[frame_index] + rolls[frame_index + 1]
        return score

    @staticmethod
    def current_frame(frames: list) -> int:
        """
        Calculate the score using current frame scoring rules (World Bowling scoring).
        """
        score = 0
        for frame in frames:
            if frame[0] == 10:  # Strike
                score += 30
            elif sum(frame) == 10:  # Spare
                score += 10 + frame[0]
            else:
                score += sum(frame)
        return score

    @staticmethod
    def nine_pin_no_tap(frames: list) -> int:
        """
        Calculate the score for a 9-pin no-tap game.
        """
        score = 0
        for i, frame in enumerate(frames):
            first_roll = frame[0]
            if first_roll == 9 or first_roll == 10:
                if i < 9:  # not the last frame
                    next_frame = frames[i + 1]
                    score += 10 + next_frame[0] + (next_frame[1] if len(next_frame) > 1 else 0)
                else:  # Last frame
                    score += 10 + frame[1] + frame[2]
            elif sum(frame[:2]) == 10:  # Spare
                score += 10 + frames[i + 1][0] if i < 9 else 10 + frame[2]
            else:
                score += sum(frame)
        return score

    @staticmethod
    def calculate_average_score(scores: list) -> float:
        """
        Calculate the average score from a list of scores.
        """
        if scores:
            return sum(scores) / len(scores)
        return 0

    @staticmethod
    def calculate_strike_percentage(frames: list) -> float:
        """
        Calculate the percentage of frames that resulted in strikes.
        """
        strikes = sum(1 for frame in frames if frame[0] == 10)
        return (strikes / len(frames)) * 100 if frames else 0

    @staticmethod
    def calculate_spare_percentage(frames: list) -> float:
        """
        Calculate the percentage of frames that resulted in spares.
        """
        spares = sum(1 for frame in frames if sum(frame[:2]) == 10 and frame[0] != 10)
        return (spares / len(frames)) * 100 if frames else 0
