def hanoi(n, rod0, rod1, rod2):
    # This is the base case, we just have to move the 1 remaining plate to the target plate
    if n == 1:
        print('Plate 1 from {} to {}'.format(rod0, rod2))
        return
    # We have to first move n-1 plates to the auxiliary rod
    hanoi(n-1, rod0, rod2, rod1)
    # Moving the largest plate from first rod to the target rod
    print('Plate {} from {} to {}'.format(n, rod0, rod2))
    # Placing n-1 rods on top of the largest rod
    hanoi(n-1, rod1, rod0, rod2)

if __name__ == '__main__':
    hanoi(3, 'A', 'B', 'C')
