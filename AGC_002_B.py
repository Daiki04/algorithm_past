N, M = map(int, input().split())

Flag = [False] * N
Balls = [1] * N
Flag[0] = True

for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if Flag[x]:
        Flag[y] = True
        if Balls[x] == 1:
            Flag[x] = False
    Balls[x] -= 1
    Balls[y] += 1
print(sum(Flag))