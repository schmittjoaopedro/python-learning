def heapRecPerm(array, n):
    i = 0
    while True:
        if n > 2:
            heapRecPerm(array, n - 1)
        if i == n - 1:
            break
        if n % 2 == 0:
            array[i], array[n - 1] = array[n - 1], array[i]
            print(array)
        else:
            array[0], array[n - 1] = array[n - 1], array[0]
            print(array)
        i += 1


def heap(array, n):
    print(array)
    heapRecPerm(array, n)


array = [1, 2, 3, 4, 5, 6]
heap(array, len(array))
