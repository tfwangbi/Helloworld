def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1

    return result


if __name__ == "__main__":
    print(factorial(10))
    print(factorial(3))
