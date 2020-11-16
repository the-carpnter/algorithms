# Iterative Solution
def consonants(string):
    count = 0
    for i, ch in enumerate(string):
        if ch.isalpha() and ch.lower() not in 'aeiou':
            count += 1
    return 'The no of consonants: ' + str(count)

# Recursive Solution
def cons(string, i=0, count=0):
    if string[i].isalpha() and string[i].lower() not in 'aeiou':
        count += 1
    if i == len(string) - 1:
        return 'The no of consonants: ' + str(count)
    return cons(string, i+1, count)

# Recursive Solution2
def cons2(string):
    if string == '':
        return 0
    if string[0].isalpha() and string[0].lower() not in 'aeiou':
        return 1 + cons2(string[1:])
    else:
        return cons2(string[1:])


if __name__=='__main__':
    string = 'AEIOUxyZ1'
    print(consonants(string))
    print(cons(string))
    print(cons2(string))