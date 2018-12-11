#!/usr/bin/env python3

from math import log, floor

N = 10001 
search_range = (2, floor(N*(log(N)**2)))
# print(search_range)

sieve = [True for i in range(*search_range)]

for num in range(*search_range):
    for candidate in range(num, search_range[1],num):
        if candidate == num:
            continue
        sieve[candidate - search_range[0]] = False

prime_count = 0
for i, isprime in enumerate(sieve):
    # print(prime_count + 1, i + search_range[0], isprime)
    prime_count += isprime
    if prime_count == N:
        print(i + search_range[0])
        break
