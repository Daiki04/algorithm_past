N = int(input())
S = list(map(int, input().split()))
A = []
total = 0

for s in S:
    a = s - total
    A.append(a)
    total += a
A = list(map(str, A))

print(" ".join(A))