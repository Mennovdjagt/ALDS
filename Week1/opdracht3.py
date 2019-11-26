def between(a, max):
    result = []
    for i in range(0, int((len(a)/2))):
        j = len(a)-i-1
        sum = 0
        for k in range(i, j):
            print('before ' + str(sum))
            sum = sum + a[k]
            print('after ' + str(sum))
        if sum > max:
            sum = max
            print(sum)
        print('in result ' + str(sum))
        result.append(sum)
    return result


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max = 10
print(between(a, max))