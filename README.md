# TrueRoll: Ten-Pin Bowling Simulation

TrueRoll is a Python library for simulating ten-pin bowling games, including
different scoring systems and statistical analysis of games. The project also
allows simulating various bowlers and alleys to study how different conditions
affect the game outcomes.

## Features

- Simulate ten-pin bowling games with customizable player and alley
  characteristics.
- Supports traditional scoring, current frame scoring, and 9-pin no-tap scoring
  systems.
- Analyze game statistics such as average scores, strike percentages, and spare
  percentages.
- Store and retrieve game, bowler, and alley data using a SQLite database for
  historical analysis.

## Installation

TrueRoll requires Python 3.7+.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourgithubusername/trueroll.git
   cd trueroll
   ```

2. Install the project with Poetry:
   ```bash
   poetry install
   ```

This will install all necessary dependencies and set up a virtual environment.

## Usage

To start simulating bowling games, you can use the modules provided in the
`trueroll` package. Here is a simple example:

```python
from trueroll.bowler import Bowler
from trueroll.game import Game
from trueroll.alley import Alley

# Create instances of Bowler and Alley
bowler = Bowler(name="John Doe", handedness="Left", style="Two-handed")
alley = Alley(name="High Strike Bowling", location="Downtown", lane_type="Synthetic")

# Simulate a game
game = Game(bowler, alley)
results = game.run_simulation()
print(results)
```

## Testing

Run tests using pytest:
```bash
poetry run pytest
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests, suggest
features, or report bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
for details.
