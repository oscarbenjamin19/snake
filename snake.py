import msvcrt
import os
import random
import time
import sys

WIDTH  = 40
HEIGHT = 20

def clear():
    os.system("cls")

def get_key():
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'\xe0':  # arrow key prefix
            key = msvcrt.getch()
            return {b'H': 'UP', b'P': 'DOWN', b'K': 'LEFT', b'M': 'RIGHT'}.get(key)
        if key == b'q':
            return 'QUIT'
        if key in (b's', b'S'):
            return 'RESTART'
    return None

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

    # move cursor to top instead of clearing (smoother)
    sys.stdout.write("\033[H" + "\n".join(lines) + "\n")
    sys.stdout.flush()

def place_food(snake):
    while True:
        pos = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))
        if pos not in snake:
            return pos

def game_loop():
    snake = [(HEIGHT // 2, WIDTH // 2), (HEIGHT // 2, WIDTH // 2 - 1)]
    direction = (0, 1)
    food = place_food(snake)
    score = 0
    speed = 0.15

    while True:
        key = get_key()
        if key == 'QUIT':
            return False
        elif key == 'UP'    and direction != (1, 0):  direction = (-1, 0)
        elif key == 'DOWN'  and direction != (-1, 0): direction = (1, 0)
        elif key == 'LEFT'  and direction != (0, 1):  direction = (0, -1)
        elif key == 'RIGHT' and direction != (0, -1): direction = (0, 1)

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if not (0 <= head[0] < HEIGHT and 0 <= head[1] < WIDTH) or head in snake:
            break

        snake.insert(0, head)

        if head == food:
            score += 10
            food = place_food(snake)
            speed = max(0.05, speed - 0.005)
        else:
            snake.pop()

        draw(snake, food, score)
        time.sleep(speed)

    clear()
    print("=" * (WIDTH + 2))
    print("  *** GAME OVER ***")
    print(f"  Dein Score: {score}")
    print("  [S] Neu starten   [Q] Beenden")
    print("=" * (WIDTH + 2))

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().lower()
            if key == b's':
                return True
            if key == b'q':
                return False


def main():
    os.system("cls")
    # enable ANSI escape codes on Windows
    os.system("")

    while game_loop():
        os.system("cls")

if __name__ == "__main__":
    main()
