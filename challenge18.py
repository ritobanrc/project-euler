#!/usr/bin/env python3

triangle = (
'''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23''')


triangle = [[int(i) for i in l.split(' ')] for l in triangle.split('\n')]
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

print('\n'.join([str(l) for l in longest_paths]))
print(max(longest_paths[-1]))
