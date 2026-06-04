import os
import sys

from .config import WIDTH, HEIGHT

def clear():
    os.system("cls")

def draw(snake, food, score):
    grid = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]
    fy, fx = food
    grid[fy][fx] = "@"
    for i, (y, x) in enumerate(snake):
        grid[y][x] = "O" if i == 0 else "o"

    lines = ["+" + "-" * WIDTH + "+"]
    for row in grid:
        lines.append("|" + "".join(row) + "|")
    lines.append("+" + "-" * WIDTH + "+")
    lines.append(f"  Score: {score}   [Pfeiltasten] bewegen   [Q] beenden")

    sys.stdout.write("\033[H" + "\n".join(lines) + "\n")
    sys.stdout.flush()
