def fibonacci_growth(n):
    #base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    #recursive case
    return fibonacci_growth(n - 2) + fibonacci_growth(n - 1)
print(fibonacci_growth(5))
print(fibonacci_growth(8))
