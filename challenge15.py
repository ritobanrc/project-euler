#!/usr/bin/env python3

import numpy as np
from collections import deque

grid = np.zeros((20 + 1, 20 + 1))

grid[0, 0] = 1

for x in range(grid.shape[0]):
    for y in range(grid.shape[1]):
        if x > 0:
            grid[x,y] += grid[x-1, y]
        if y > 0:
            grid[x, y] += grid[x, y-1]

# print(grid)
print(int(grid[grid.shape[0] - 1, grid.shape[1] - 1]))
