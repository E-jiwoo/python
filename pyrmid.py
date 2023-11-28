n = int(input())
total = n * (n + 1) // 2
for i in range(1, n + 1):
    for j in range(i):
        print(total, end=" ")
        total -= 1
    print()
