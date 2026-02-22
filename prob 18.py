def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return list(map(int, str(result)))


# Example
print(factorial(10))  # Output: [3,6,2,8,8,0,0]