def fibonacci_step1(n):
    if n <= 1:
        return 1
    return fibonacci_step1(n-1) + fibonacci_step1(n-2)


def main():
    for f in range(10):
        print(fibonacci_step1(f))


if __name__ == "__main__":
    main()
