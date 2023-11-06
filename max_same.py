"""
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
"""

a, b = map(int, input().split())

while b != 0:
    r = a % b
    a, b = b, r

print(a)
