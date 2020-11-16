def product(a, b, acc=0):
    if b == 0:
        return acc
    return product(a, b - 1, acc+a)

def multiply(a, b):
    if a<b:
        return multiply(b,a)
    if b == 0:
        return 0
    return a + multiply(a, b-1)

if __name__ == '__main__':
    print(product(5, 3))
    print(multiply(5, 3))