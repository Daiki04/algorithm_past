A, B, C, D, E, F, X = map(int, input().split())

t = 0
a = 0

def dis(s, m, u):
    n = 0
    n += (X // (s + u)) * (s * m)

    if X % (s + u) <= s:
        n += X % (s + u) * m
    else:
        n += s * m
    return n

t = dis(A, B, C)
a = dis(D, E, F)


if a == t:
    print('Draw')
elif a > t:
    print('Aoki')
else:
    print('Takahashi')