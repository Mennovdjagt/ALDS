def prime():
    """Function that will return all the prime numbers till 1000.

            Returns:
                The return value is a list of all the prime numbers.
        """
    array = []
    for i in range(2, 1000):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0 or i == 2 or i == 3 or i == 5 or i == 7 or i == 11:
            array.append(i)
    return array


def prime1():
    array = []
    for i in range(2, 1000):
        check = True
        for j in range(0, i):
            for k in range(0, i):
                if (j*k) == i:
                    check = False
                    break
            if not check:
                break
        if check:
            array.append(i)
    return array


def prime2():
    array = []
    for i in range(2, 1000):
        check = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                check = False
                break
        if check:
            array.append(i)
    return array


print(prime())
print(prime1())
print(prime2())
