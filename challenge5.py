#!/usr/bin/env python3
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a*b/gcd(a,b)


def main():
    num = 1
    for i in range(1, 20):
        num = lcm(num, i)
    print(num)


if __name__ == '__main__':
    main()
