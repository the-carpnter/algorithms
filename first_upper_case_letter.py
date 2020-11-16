# Iterative Solution
def findi(string):
    for i,c in enumerate(string):
        if c.isupper():
            return 'The position is : ' + str(i)
    return 'Not Found!'

# Recursive Solution
def findr(string, i=0):
    if string[i].isupper():
        return 'The position is : ' + str(i)
    if i == len(string) - 1:
        return 'Not Found'
    return findr(string, i+1)

if __name__ == '__main__':
    s = 'i am a good Boy'
    print(findi(s))
    print(findr(s))