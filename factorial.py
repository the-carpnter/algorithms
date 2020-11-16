# This is head recursion
def factorial(n):
    if n == 1:
        return 1
    
    subresult = factorial(n-1)
    result = n * subresult
    return result

# This is tail recursion
def fact_acc(n, accumulator=1):
    if n == 1:
        return accumulator
    
    return fact_acc(n-1, n*accumulator)

print(factorial(5))
print(fact_acc(5))