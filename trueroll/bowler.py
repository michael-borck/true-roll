class Bowler:
    def __init__(self, name: str, strike_prob: float, spare_prob: float, handedness: str = 'right', technique: str = 'single'):
        """
        Initializes a Bowler with specific characteristics and probabilities for bowling actions.
        
        :param name: The name of the bowler.
        :param strike_prob: Probability of hitting a strike.
        :param spare_prob: Probability of hitting a spare.
        :param handedness: The preferred hand of the bowler ('left' or 'right').
        :param technique: The bowling technique used ('single' or 'double' handed).
        """
        self.name = name
        self.strike_prob = strike_prob
        self.spare_prob = spare_prob
        self.handedness = handedness
        self.technique = technique

    def __str__(self):
        return (f"Bowler(Name: {self.name}, Strike Probability: {self.strike_prob}, "
                f"Spare Probability: {self.spare_prob}, Handedness: {self.handedness}, "
                f"Technique: {self.technique})")
