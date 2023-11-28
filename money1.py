remain = int(input())
change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
cnt = 0

for i in range(0, 9, +1):
    cnt += remain
    remain %= int(change[i])

print(cnt)
