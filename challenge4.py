def main():
    highest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            ij = i*j
            s = str(ij)
            if s == s[::-1]:
                if ij > highest:
                    highest = ij
    print(highest)


if __name__ == '__main__':
    main()