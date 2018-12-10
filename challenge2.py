def main():
    fib = [1, 2]
    while fib[-1] < 4*10**6:
        fib.append(fib[-1] + fib[-2])
    print(sum([i if i % 2 == 0 else 0 for i in fib]))


if __name__ == '__main__':
    main()