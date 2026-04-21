import numpy as np
import matplotlib.pyplot as plt
from components import Component
from patterns import GOSPER_GUN

def step(grid):
    rows, cols = grid.shape

    padded = np.pad(grid, pad_width=1, mode='constant', constant_values=0)

    neighbors = (
        padded[0:rows,   0:cols]   + padded[0:rows,   1:cols+1] + padded[0:rows,   2:cols+2] +
        padded[1:rows+1, 0:cols]                                + padded[1:rows+1, 2:cols+2] +
        padded[2:rows+2, 0:cols]   + padded[2:rows+2, 1:cols+1] + padded[2:rows+2, 2:cols+2]

    )

    return ((neighbors == 3) | ((grid == 1) & (neighbors == 2))).astype(np.uint8)

def place_pattern(grid, pattern, top=0, left=0):
    for r, c in pattern:
        grid[top + r, left + c] = 1

grid = np.zeros((500, 500), dtype=np.uint8)
#grid = np.random.randint(0, 2, (200, 200), dtype=np.uint8)
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