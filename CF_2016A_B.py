N = int(input())
A = list(map(int, input().split()))
ans = 0

Flag = [False] * N

for i in range(N):
    if A[A[i]-1] == i+1 and not Flag[A[i]-1]:
        ans += 1
    
    Flag[i] = True

print(ans)