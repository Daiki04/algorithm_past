N = int(input())
A = list(map(int, input().split()))

a1 = sum(A) // N
a2 = a1 + 1

INF = 10 ** 9
ans = sum((a - a1) ** 2 for a in A)
ans2 = sum((a - a2) ** 2 for a in A)

print(min(ans, ans2))