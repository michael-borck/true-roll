# Command Line Interface

TrueRoll provides a comprehensive command-line interface (CLI) built with Typer, offering rich command-line functionality with subcommands, options, and help documentation.

## Installation

The CLI is automatically installed when you install TrueRoll:

```bash
pip install trueroll
```

## Command Structure

TrueRoll's CLI follows a subcommand structure:

```
trueroll [command] [subcommand] [options] [arguments]
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
trueroll --help
```

## Bowler Management

### List bowlers

```bash
trueroll bowlers list
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
trueroll bowlers add "John Doe" 180
```

### Get help on bowler commands

```bash
trueroll bowlers --help
```

## Game Management

### List games

```bash
trueroll games list
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
trueroll games add "John Doe" 210
```

### Get help on game commands

```bash
trueroll games --help
```

## League Management

### List leagues

```bash
trueroll leagues list
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
trueroll leagues add "Monday Night League"
```

### Get help on league commands

```bash
trueroll leagues --help
```

## TUI Interface

Start the Terminal User Interface:

```bash
trueroll tui start
```

## Web Interface

Start the Web Interface:

```bash
trueroll web start
```

With custom host and port:

```bash
trueroll web start --host 0.0.0.0 --port 8080
```

Enable debug mode:

```bash
trueroll web start --debug
```

## Python API Access

You can also access the CLI programmatically from Python:

```python
import trueroll
trueroll.run_cli()
```

This is equivalent to running the `trueroll` command in the terminal.

## Advanced Usage

### Environment Variables

TrueRoll CLI also respects environment variables. Any option can be set using an environment variable with the prefix `TRUEROLL_` followed by the option name in uppercase.

For example:
- `--host` can be set with `TRUEROLL_HOST`
- `--port` can be set with `TRUEROLL_PORT`

```bash
export TRUEROLL_HOST=0.0.0.0
export TRUEROLL_PORT=8080
trueroll web start
```