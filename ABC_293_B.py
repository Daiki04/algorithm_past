N = int(input())
A = list(map(int, input().split()))

flag = [True] * N

for i in range(N):
    if flag[i]:
        flag[A[i]-1] = False

print(sum(flag))
for i in range(N):
    if flag[i]:
        print(i+1, end = " ")