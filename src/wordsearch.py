import random
import numpy as np
import matplotlib.pyplot as plt

def generate_wordsearch(words, grid_size=15):
    grid = [[" " for _ in range(grid_size)] for _ in range(grid_size)]

    for word in words:
        word = word.upper()
        placed = False
        while not placed:
            direction = random.choice(["H", "V"])
            if direction == "H":
                row = random.randint(0, grid_size-1)
                col = random.randint(0, grid_size-len(word))
                if all(grid[row][col+i] in (" ", word[i]) for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row][col+i] = word[i]
                    placed = True
            else:  # vertical
                row = random.randint(0, grid_size-llen(word))
                col = random.randint(0, grid_size-1)
                if all(grid[row+i][col] in (" ", word[i]) for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row+i][col] = word[i]
                    placed = True

    # Fill empty spots with random letters
    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] == " ":
                grid[r][c] = chr(random.randint(65, 90))

    return np.array(grid)

def save_wordsearch(grid, output_path="assets/puzzle_output.png"):
    plt.figure(figsize=(8, 8))
    plt.table(cellText=grid, loc="center", cellLoc="center", edges="closed")
    plt.axis("off")
    plt.savefig(output_path)
    plt.close()
    return output_path
