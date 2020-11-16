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

if __name__=='__main__':
    string = 'AEIOUxyZ1'
    print(consonants(string))
    print(cons(string))