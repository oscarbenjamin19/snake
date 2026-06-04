import os
import random
import time

from .config import WIDTH, HEIGHT
from .input import get_key
from .renderer import clear, draw

def place_food(snake):
    while True:
        pos = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))
        if pos not in snake:
            return pos

def main():
    os.system("cls")
    os.system("")

    snake = [(HEIGHT // 2, WIDTH // 2), (HEIGHT // 2, WIDTH // 2 - 1)]
    direction = (0, 1)
    food = place_food(snake)
    score = 0
    speed = 0.15

    while True:
        key = get_key()
        if key == 'QUIT':
            break
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
    print("=" * (WIDTH + 2))

if __name__ == "__main__":
    main()
