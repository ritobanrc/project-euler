#!/usr/bin/env python3


with open('challenge67_data.txt', 'r') as f:
    triangle = [[int(i) for i in l.split(' ')] for l in f.readlines()]

longest_paths = [[0] * (i+1) for i in range(len(triangle))]

# edges between x and x + 1
# Algorithm:
    # Start at top
    # Go to each branch, make note of the longest path to get to that point
    # find the longest path in the bottom row

longest_paths[0][0] = triangle[0][0]
# now, each location has up to 2 sources (x and/or x-1, y-1)
# we can set the cost to arrive at each location the greater of the source + that locations cost

for y, row in enumerate(triangle):
    if y == 0:
        continue
    for x, n in enumerate(row):
        total_cost1 = 0
        total_cost2 = 0
        total_cost1 = n + longest_paths[y-1][x-1]
        try: 
            total_cost2 = n + longest_paths[y-1][x]
        except IndexError:
            pass
        longest_paths[y][x] = max(total_cost1, total_cost2)

# print('\n'.join([str(l) for l in longest_paths]))
print(max(longest_paths[-1]))
