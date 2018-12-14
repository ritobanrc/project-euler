#!/usr/bin/env python3

a = 1
for i in range(1, 100):
    a *= i

print(sum(int(d) for d in str(a)))
