n = input()
rev_n = n[::-1]
sum = int(n) + int(rev_n)
if str(sum) == str(sum)[::-1]:
    print("YES")
else:
    print("NO")
