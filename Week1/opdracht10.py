a = [],[]


def money(x, b):
    m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

    if x == m[b-1]:
        print(b-1)
        a[b-1].append(1)
        return
    elif x < m[b-1]:
        return
    else:
        total = 0
        rest = x - m[b-1]
        for i in range(0, b - 1):
            if rest <= m[i]:
                if rest == m[i]:
                    ++total
                elif rest % m[i] == 0:
                    ++total
        if len(a[b-1]) == x:
                a[b-1].append(total + a[b-1][x-1])
        else:
            a[b - 1].append(total)
    return

def money1(x, b):
    m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    if len(a) < b-1:



        print(a)
    print(len(a))

    #rest = x - m[s]

    return


for i in range(0, 10):
    for j in range(1, 10):
        print(a)
        money(j, i)
