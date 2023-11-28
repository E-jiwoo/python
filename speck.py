def a(num):
    sum = num + int(str(num)[::-1])
    return 'YES' if str(sum) == str(sum)[::-1] else 'NO'
    
num = int(input)
print(a(num))

def a(num):
    sum = num + int(str(num)[::-1])
    return 'YES' if str(sum) == str(sum)[::-1] else 'NO'

num = int(input())
print(a(num))