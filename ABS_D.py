N = int(input())
A = list(map(int, input().split()))
ans = 0
flag = False

while True:
    for i in range(N):
        if A[i] % 2 != 0 or A[i] == 0:
            flag = True
            break
        else:
            A[i] = A[i] / 2
    
    if flag:
        break
    else:
        ans += 1

print(ans)
