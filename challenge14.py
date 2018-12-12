#!/usr/bin/env python3

import time

longest_number = 0
longest_length = 0  # not counting 1

memo = {}

start = time.time()

for i in range(10**6):
    count = 0
    n = i
    while n > 1:
        if n in memo:
            count += memo[n]
            break
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        count += 1

    memo[i] = count
    if count > longest_length:
        longest_length = count
        longest_number = i
        print(longest_number, longest_length)

end = time.time()

print(longest_number, ' in ', end - start, ' seconds')

