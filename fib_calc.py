def fibonacci(n):
    if type(n) is not int:
        return -1
    if n <= 0 or n >= 10001:
        return -1
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n - 1):
            result = a + b
            a = b
            b = result
        return result