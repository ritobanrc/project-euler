#!/usr/bin/env python3

longest_number = 0
longest_length = 0

for i in range(10**6):
    count = 0
    n = i
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        count += 1
    if count > longest_length:
        longest_length = count
        longest_number = i

print(longest_number)

