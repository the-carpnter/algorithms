def linear_search(array, lookup):
    # Simple Linear Search in O(N) running time complexity
    for i, item in enumerate(array):
        # We return the index if the item matches the lookup value
        if item == lookup:
            return i
    # If we don't find any item
    return -1

if __name__ == '__main__':
    array = [1, 4, 3, 22, 5, 6, 7, 8]
    print(linear_search(array, 5))