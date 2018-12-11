#!/usr/bin/env python3
def main():
    squaresum = 0
    sumsquare = 0
    for i in range(1, 101):
        squaresum += i
        sumsquare += i*i
    squaresum *= squaresum
    print(squaresum - sumsquare)


if __name__ == '__main__':
    main()
