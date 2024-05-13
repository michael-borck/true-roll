class Alley:
    def __init__(self, lane_type: str, oil_pattern: str):
        """
        Initialize an alley with specified lane type and oil pattern characteristics.
        
        :param lane_type: Type of the lane (e.g., 'synthetic', 'wood').
        :param oil_pattern: Type of oil pattern applied to the lane (e.g., 'heavy', 'medium', 'light').
        """
        self.lane_type = lane_type
        self.oil_pattern = oil_pattern

    def __str__(self):
        return f"Alley(Lane Type: {self.lane_type}, Oil Pattern: {self.oil_pattern})"
