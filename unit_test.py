from fib_calc import fibonacci

def test_fibonacci(n, expected):
  result = fibonacci(n)
  if result == expected:
    print("OK: n= ", n, " result =", result, ", expected =", expected)
  else:
    print("NG: n= ", n, " result =", result, ", expected =", expected)
  
# 適切なnのケース
test_fibonacci(1, 1)
test_fibonacci(2, 1)
test_fibonacci(10, 55)
test_fibonacci(11, 89)

# 不適切なnのケース
test_fibonacci(0, -1)
test_fibonacci(-1, -1)
test_fibonacci(0.5, -1)
test_fibonacci("あ", -1)
test_fibonacci(10001, -1)
test_fibonacci(True, -1)
test_fibonacci(1.0, -1)
test_fibonacci(None, -1)
test_fibonacci(" ", -1)
