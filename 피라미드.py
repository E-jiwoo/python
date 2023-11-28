def f(n):
    if n == 1:
        return 1
    return n + f(n - 1)


n = int(input())
n2 = f(n)

for i in range(n):
    for j in range(i + 1):
        print(n2, end=" ")
        n2 -= 1
    print()
