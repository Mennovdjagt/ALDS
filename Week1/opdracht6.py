def avgHairLength(a):
    sum = 0

    print(a)

    for i in a:
        sum = sum + i
    result = sum / len(a)
    return result


def hairyGroupsOf3(arr):
    result = [(), (), ()]
    m = 0

    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)-1):
                tup = (arr[i], arr[j], arr[k])
                relativeHair = avgHairLength(tup) - avgHairLength(list(set(arr)-set(tup)))
                result[m] = (tup, relativeHair)
                m += 1
                if m > 2:
                    m = 0
    return result


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(hairyGroupsOf3(arr))
