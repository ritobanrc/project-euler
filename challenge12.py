#!/usr/bin/env python3

import math
from collections import defaultdict
import itertools

def count_divisors(n): 
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) : 
        if (n % i == 0) : 
            if (n / i == i) : 
                cnt = cnt + 1
            else : # Otherwise count both 
                cnt = cnt + 2
    return cnt 

n = 2 

while True:
    tri_num = sum([i for i in range(n)])
    num_factors = count_divisors(tri_num) 
    if num_factors > 500:
        print(tri_num)
        break
    n += 1
