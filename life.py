import numpy as np
import matplotlib.pyplot as plt
from components import Component
from patterns import GOSPER_GUN

def step(grid):
    neighbors = sum(
        np.roll(np.roll(grid, i, 0), j, 1)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        if not (i == 0 and j == 0)
    )

    return ((neighbors == 3) | ((grid == 1) & (neighbors == 2))).astype(np.uint8)

def place_pattern(grid, pattern, top=0, left=0):
    for r, c in pattern:
        grid[top + r, left + c] = 1

grid = np.zeros((500, 500), dtype=np.uint8)
place_pattern(grid, GOSPER_GUN, top=10, left=10)

plt.ion()
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='binary', interpolation='nearest')
ax.set_xticks([])
ax.set_yticks([])

for t in range(20000):
    grid = step(grid)

    if t % 2 == 0:
        img.set_data(grid)
        plt.pause(0.001)