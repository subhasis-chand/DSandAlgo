def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_n(5))


def sum_n_recursive(n):
    if n == 0:
        return 0
    return n + sum_n_recursive(n - 1)


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
# ret -> 5 * factorial_recursive(4)
#     ret -> 4 * factorial_recursive(3)
#         ret -> 3 * factorial_recursive(2)
#             ret -> 2 * factorial_recursive(1)
#                 ret -> 1


def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursive(n):
    print('inside fib: ', n)
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# print(sum_n(5))              # 15
# print(sum_n_recursive(5))    # 15

# print(factorial(5))          # 120
# print(factorial_recursive(5))# 120

# print(fibonacci(7))          # 13
print(fibonacci_recursive(7))# 13