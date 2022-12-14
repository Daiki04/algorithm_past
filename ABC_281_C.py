N, T = map(int, input().split())
A = list(map(int, input().split()))

sum = 0

for a in A:
    sum += a

t = T % sum

for i in range(N):
    if t - A[i] < 0:
        print(f"{i+1} {t}")
        break
    t -= A[i]