a = int(input())
count = 0
f, j, e, i, q, s, d, z = 1, 1, 1, 1, 1, 1, 1, 1
while f != 0:
    if i != 0:
        count = count + 1
        a = a % 50000
        i = a // 50000

    if q != 0:
        count = count + 1
        a = a % 10000
        q = a // 10000

    if s != 0:
        count = count + 1
        a = a % 5000
        s = a // 5000

    if j != 0:
        count = count + 1
        a = a % 1000
        j = a // 1000

    if e != 0:
        count = count + 1
        a = a % 500
        e = a // 500

    if z != 0:
        count = count + 1
        a = a % 500
        z = a // 500

    if d != 0:
        count = count + 1
        a = a % 50
        d = a // 50

    if f != 0:
        count = count + 1
        a = a % 10
        f = a // 10

print(count)
