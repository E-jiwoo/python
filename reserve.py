# 거꾸로 출력 방법
"""
S = "abcde"
for i in range(len(S) - 1, -1, -1):
    print(S[i], end="")
"""
S = "abcde"
rev_S = ""
for i in S:  # i는 S랑 같은 형이여서 문자형이됨
    rev_S = i + rev_S
    print(rev_S)
"""
a+''  a
b+a ba
c+ ba cba
"""
