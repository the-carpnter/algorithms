# This is head recursion
def natural(n):
    if n == 0:
        return
    natural(n-1)
    print(n)
    

# This is tail recursion
def nat(n):
    if n == 0:
        return
    print(n)
    natural(n-1)

natural(10)
    