from random import seed
from random import randint


def min(x):
    length = len(x)
    return x[int(length/2)]


def partition(x, lo, hi):
    """function that puts a smaller number on the left and the bigger number on the right

    Args:
        x: an unsorted array
        lo: first index of the list you want to sort
        hi: last index of the list you want to sort

    Returns:
        x: a sorted array where higher and lower numbers are swapped

    Examples:

    """
    pivot = min(x[lo:hi+1])
    index = x.index(pivot)
    x[hi], x[index] = x[index], x[hi]
    i = lo - 1
    compares = 0
    for j in range(lo, hi):
        compares += 1
        if x[j] <= pivot:
            i += 1
            x[i], x[j] = x[j], x[i]
    x[i+1], x[hi] = x[hi], x[i+1]
    return i+1, compares


def quick_sort(x, lo, hi):
    """function that returns a sorted list between lo and hi

    Args:
        x: an unsorted array
        lo: first index of the list you want to sort
        hi: last index of the list you want to sort

    Returns:
        x: a sorted array between hi and lo

    Examples:
        array = [5,4,8,6]
        >>> print(quick_sort(array, 0, 3))
        [4, 5, 6, 8]

    """
    count = [[], [], []]

    if lo >= hi:
        return x, 1

    p, count[0] = partition(x, lo, hi)
    x, count[1] = quick_sort(x, lo, p-1)
    x, count[2] = quick_sort(x, p+1, hi)
    return x, sum(count)


seed(1)

for i in range(0, 100):
    array = []
    for j in range(0, 10):
        array.append(randint(1, 100))
    print(quick_sort(array, 0, len(array) - 1))

