# Command Line Interface

TrueRoll provides a comprehensive command-line interface (CLI) built with Typer, offering rich command-line functionality with subcommands, options, and help documentation.

## Installation

The CLI is automatically installed when you install TrueRoll:

```bash
pip install true-roll
```

## Command Structure

TrueRoll's CLI follows a subcommand structure:

```
true-roll [command] [subcommand] [options] [arguments]
```

Main commands include:

- `bowlers` - Manage bowlers
- `games` - Manage games
- `leagues` - Manage leagues
- `tui` - Access the Terminal User Interface
- `web` - Access the Web Interface

## Global Help

To see all available commands:

```bash
true-roll --help
```

## Bowler Management

### List bowlers

```bash
true-roll bowlers list
```

Example output:
```
┏━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Name        ┃ Average ┃
┡━━━━━━━━━━━━╇━━━━━━━━━┩
│ John Doe    │ 180     │
│ Jane Smith  │ 210     │
│ Bob Johnson │ 160     │
└─────────────┴─────────┘
```

### Add a bowler

```bash
true-roll bowlers add "John Doe" 180
```

### Get help on bowler commands

```bash
true-roll bowlers --help
```

## Game Management

### List games

```bash
true-roll games list
```

Example output:
```
┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━┓
┃ Date        ┃ Bowler     ┃ Score ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━┩
│ 2023-05-01  │ John Doe   │ 185   │
│ 2023-05-02  │ Jane Smith │ 215   │
│ 2023-05-03  │ Bob Johnson│ 155   │
└─────────────┴────────────┴───────┘
```

### Add a game

```bash
true-roll games add "John Doe" 210
```

### Get help on game commands

```bash
true-roll games --help
```

## League Management

### List leagues

```bash
true-roll leagues list
```

Example output:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Name                    ┃ Members ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ Friday Night League     │ 12      │
│ Sunday Afternoon League │ 8       │
└─────────────────────────┴─────────┘
```

### Add a league

```bash
true-roll leagues add "Monday Night League"
```

### Get help on league commands

```bash
true-roll leagues --help
```

## TUI Interface

Start the Terminal User Interface:

```bash
true-roll tui start
```

## Web Interface

Start the Web Interface:

```bash
true-roll web start
```

With custom host and port:

```bash
true-roll web start --host 0.0.0.0 --port 8080
```

Enable debug mode:

```bash
true-roll web start --debug
```

## Python API Access

You can also access the CLI programmatically from Python:

```python
import true_roll
true_roll.run_cli()
```

This is equivalent to running the `true-roll` command in the terminal.

## Advanced Usage

### Environment Variables

TrueRoll CLI also respects environment variables. Any option can be set using an environment variable with the prefix `TRUE_ROLL_` followed by the option name in uppercase.

For example:
- `--host` can be set with `TRUE_ROLL_HOST`
- `--port` can be set with `TRUE_ROLL_PORT`

```bash
export TRUE_ROLL_HOST=0.0.0.0
export TRUE_ROLL_PORT=8080
true-roll web start
```