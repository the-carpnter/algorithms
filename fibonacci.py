# This is head recursion
def fibonacci(n):
    if n in {0,1}:
        return n
    fib_1 = fibonacci(n-1)
    fib_2 = fibonacci(n-2)
    result = fib_1 + fib_2
    return result

# This is tail recursion
def fib(n, a=0, b=1):
    if n == 0: return a
    if n == 1: return b
    return fib(n-1, b, a+b)


if __name__ == '__main__':
    print(fibonacci(10))
    print(fib(100))