import math

T = int(input())

def factorization(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    return prime

for _ in range(T):
    N = int(input())
    A = factorization(N)
    n = [0, 0]

    if (A[0] ** 2) * A[1] == N:
        n[0] = A[0]
        n[1] = A[1]
    else:
        n[0] = A[1]
        n[1] = A[0] 

    print(*n)
