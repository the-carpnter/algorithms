# Iterative Approach
def bin_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high)//2
        if array[mid]==item:
            return 'The item found at index: ' + str(mid)
        if item > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return 'Item not found!'


# Recursive Approach
def binary_search(array, item, left, right):

    # base case of recursive function calls
    # this happens when the array does not contain the item
    if right <  left:
        print('Item not found!')
        return -1

    # computing the middle item's index
    middle = left + (right - left)//2
    print('Middle Index: {}'.format(middle))

    # if the middle item matches
    if array[middle] == item:
        print('Found the item!')
        return middle
    
    # if the item we are looking for is smaller than the middle item
    # we have to consider the left array
    elif array[middle] > item:
        print('Checking items on the left...')
        return binary_search(array, item, left, middle-1)
    
    # if the item we are looking for is greater than the middle item
    # we have to consider the right array
    elif array[middle] < item:
        print('Checking items on the right...')
        return binary_search(array, item, middle+1, right)
    
if __name__ == '__main__':
    print(bin_search(range(100), 23))
    print(binary_search(range(100), 23, 0, 99))