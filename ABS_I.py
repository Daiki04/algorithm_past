N, Y = map(int, input().split())
flag = False
ans = [-1, -1, -1]

for i in range(N+1):
    for j in range((N-i)+1):
        m = 10000*i + 5000*j + 1000*(N-i-j)
        if m == Y:
            ans = [i, j, N-i-j]
            flag=True
            break
    if flag:
        break

print(*ans)