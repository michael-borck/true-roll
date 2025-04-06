# TrueRoll Interfaces

TrueRoll provides multiple interfaces to interact with the bowling simulation library, allowing you to choose the most appropriate interface for your needs.

## Overview

TrueRoll offers four distinct ways to interact with the library:

1. **Python Library** - Import and use TrueRoll as a Python module
2. **Command Line Interface (CLI)** - Use the `true-roll` command in your terminal
3. **Terminal User Interface (TUI)** - Interactive terminal-based dashboard
4. **Web Interface** - Browser-based graphical interface

## Choosing an Interface

| Interface | Best For | Requires | 
|-----------|----------|----------|
| Python Library | Integration with other Python code, custom workflows | Python knowledge |
| CLI | Quick commands, scripting, automation | Terminal access |
| TUI | Interactive management on remote servers, low bandwidth connections | Modern terminal |
| Web Interface | User-friendly access, team management, visualization | Web browser |

## Python Library

The Python library interface is the core of TrueRoll, allowing direct programmatic access to all features.

```python
from true_roll import Bowler, Game, Scoring

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

For more details on the Python API, see the [API Documentation](api.md).

## Command Line Interface (CLI)

The CLI provides command-line access to TrueRoll's features through the `true-roll` command.

```bash
# List bowlers
true-roll bowlers list

# Add a new bowler
true-roll bowlers add "John Doe" 180

# Start the web interface
true-roll web start
```

For more details on the CLI, see the [CLI Documentation](cli.md).

## Terminal User Interface (TUI)

The TUI provides an interactive, dashboard-like interface directly in your terminal.

```bash
# Start the TUI
true-roll tui start
```

![TrueRoll TUI](images/tui_interface.png)

For more details on the TUI, see the [TUI Documentation](tui.md).

## Web Interface

The web interface provides a modern, browser-based graphical interface.

```bash
# Start the web server
true-roll web start
```

Then access http://localhost:8000 in your browser.

![TrueRoll Web Interface](images/web_home.png)

For more details on the web interface, see the [Web Interface Documentation](web.md).

## Switching Between Interfaces

All interfaces access the same underlying data, so you can switch between them as needed:

1. Use the CLI for quick commands and scripting
2. Launch the TUI for a more interactive experience
3. Start the web interface for team management and visualization
4. Use the Python API for custom integrations

## Interface Architecture

TrueRoll's interfaces are designed as layers on top of the core library:

```
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│  Web (FastHTML) │ │  TUI (Textual)  │ │     CLI (Typer)   │
└───────┬───────┘ └───────┬───────┘ └───────┬───────┘
        │                 │                 │
        v                 v                 v
┌─────────────────────────────────────────────────┐
│                Core TrueRoll Library             │
└─────────────────────────────────────────────────┘
```

This layered architecture ensures consistency across interfaces while allowing each interface to leverage its specific strengths.