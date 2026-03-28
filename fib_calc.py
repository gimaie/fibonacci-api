def fibonacci(n):
    if n <= 0:
        return 0
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
    
if __name__ == "__main__":
    print("n=1のとき:", fibonacci(1))
    print("n=2のとき:", fibonacci(2))
    print("n=3のとき:", fibonacci(3))
    print("n=4のとき:", fibonacci(4))
    print("n=5のとき:", fibonacci(5))
