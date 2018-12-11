#!/usr/bin/env python3
from math import ceil, sqrt


def factorize(num):
    factors = []

    while num % 2 == 0:
        factors.append(2)
        num /= 2

    for i in range(3, ceil(sqrt(num)+1), 2):
        while num % i == 0:
            factors.append(i)
            num /= i

    if num > 2:
        factors.append(num)

    return factors


def main():
    num = 600851475143
    print((factorize(num)))


if __name__ == '__main__':
    main()
