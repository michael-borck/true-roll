# Welcome to TrueRoll

TrueRoll is a comprehensive simulation library for ten-pin bowling, designed to model games, analyze player performance, and investigate the impacts of various environmental and personal factors on gameplay.

## Overview

Bowling, as a sport, involves numerous variables that can influence the outcome of a game, from the skill level of the players to the characteristics of the bowling alley. TrueRoll aims to provide a realistic and flexible simulation environment where these variables can be controlled and studied. Whether you're a data scientist, a coach, or a bowling enthusiast, TrueRoll offers tools to simulate, analyze, and understand the nuances of ten-pin bowling.

## Features

TrueRoll includes several key features:

- **Game Simulation:** Simulate complete games with detailed control over player attributes and alley conditions.
- **Scoring Systems:** Support for various scoring systems including traditional, current frame, and 9-pin no-tap.
- **Statistical Analysis:** Tools to analyze game outcomes, providing insights into performance metrics such as strike rates, spare conversions, and overall scores.
- **Data Management:** Integration with a SQLite database to store and retrieve game records, player profiles, and alley specifications for longitudinal studies and performance tracking.
- **Multiple Interfaces:** 
  - Python library for programmatic access
  - Command Line Interface (CLI) for quick commands
  - Terminal User Interface (TUI) for interactive terminal usage
  - Web Interface for a graphical user experience
- **Extensibility:** Designed with extensibility in mind, allowing users to add new types of analyses, scoring rules, or even different bowling games like duckpin or candlepin bowling.

## Getting Started

### Installation

Install TrueRoll using pip:

```bash
pip install trueroll
```

Or install from source:

```bash
git clone https://github.com/michael-borck/trueroll.git
cd trueroll
pip install -e .
```

### Basic Usage

Using TrueRoll as a Python library:

```python
from trueroll import Bowler, Game, Scoring

# Create a bowler
player = Bowler("John Doe", 180)

# Create a game
game = Game(player)
game.roll(10)  # Strike
game.roll(5)   # 5 pins
game.roll(5)   # Spare

# Get the score
score = Scoring.calculate_score(game)
print(f"{player.name}'s score: {score}")
```

Using the CLI:

```bash
# Show CLI help
trueroll --help

# List bowlers
trueroll bowlers list

# Start the web interface
trueroll web start
```

## Interfaces

TrueRoll provides multiple ways to interact with the library:

- **[Python Library](api.md)**: Import and use TrueRoll as a Python module
- **[Command Line Interface](cli.md)**: Use the `trueroll` command in your terminal
- **[Terminal User Interface](tui.md)**: Interactive terminal-based dashboard
- **[Web Interface](web.md)**: Browser-based graphical interface

For more details, see the [Interfaces Overview](interfaces.md).

## Documentation

This documentation is structured to help you find what you need:

- **Interfaces**: How to interact with TrueRoll through different interfaces
- **API Reference**: Comprehensive details about the functions and classes available in TrueRoll
- **Contributing**: How to contribute to the TrueRoll project
- **Examples**: Practical examples and case studies using TrueRoll

## Contributing

TrueRoll is an open-source project, and contributions are welcome. Check out the [contributing guidelines](contribute.md) to see how you can make a difference, whether through code, documentation, or community support.

## License

TrueRoll is released under the MIT license. This choice ensures that the software can be freely used, modified, and shared.

Thank you for visiting the TrueRoll documentation. We hope you find this project useful for your bowling simulation and analysis needs!
