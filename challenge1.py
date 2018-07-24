# Multiples of 3 and 5


def main():
    print(sum([i if (i % 3 == 0 or i % 5 == 0) else 0 for i in range(0, 1000)]))


if __name__ == '__main__':
    main()
