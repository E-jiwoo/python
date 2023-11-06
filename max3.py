def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b, c = map(int, input().split())

"""
while b != 0:
    r = a % b
    a, b = b, r
    while c != 0:
        f = a % c
        a, c = c, f
"""
print(gcd(gcd(a, b), c))
