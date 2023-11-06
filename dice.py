sum = int(input())

for i in range(1, 7, 1):
    for j in range(1, 7, 1):
        if i + j == sum:
            print(i, j)
