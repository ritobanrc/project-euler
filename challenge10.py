#!/usr/bin/env python3


search_range = (2, 2*10**6)

sieve = [True for i in range(*search_range)]

for num in range(*search_range):
    for candidate in range(num, search_range[1],num):
        if candidate == num:
            continue
        sieve[candidate - search_range[0]] = False

print(sum([search_range[0] + i if sieve[i] else 0 for i in range(len(sieve))]))
