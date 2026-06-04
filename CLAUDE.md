# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the game

Launch from the `Claude/` parent directory (one level above `snake/`):

```
python -m snake.game
```

The standalone single-file version also still works:

```
python snake/snake.py
```

## Architecture

The project is a Python package (`snake/`) split into four modules:

- `config.py` — constants (`WIDTH=40`, `HEIGHT=20`)
- `input.py` — non-blocking keyboard polling via `msvcrt` (Windows-only); returns `'UP'`, `'DOWN'`, `'LEFT'`, `'RIGHT'`, `'QUIT'`, or `None`
- `renderer.py` — terminal rendering: `clear()` runs `cls`, `draw()` redraws the full grid in-place using ANSI cursor-home (`\033[H`)
- `game.py` — game loop, collision detection, food placement, speed scaling; entry point via `if __name__ == "__main__"`

All internal imports use relative syntax (`from .config import ...`), so the package **must** be invoked with `python -m`, not as a direct script path.

## Platform constraint

`input.py` uses `msvcrt`, which is Windows-only. Any cross-platform port needs to replace `get_key()` with `readchar` or `curses`.

## Game mechanics

- Speed starts at 0.15 s/tick, decreases by 0.005 per food eaten, floored at 0.05 s/tick
- Score: +10 per food item
- Collision with wall or self ends the game immediately
