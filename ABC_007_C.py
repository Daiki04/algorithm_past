from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy_i, sx_i = sy-1, sx-1
gy_i, gx_i = gy-1, gx-1

C = [list(input()) for _ in range(R)]

Q = deque()
Q.append([0, sy_i, sx_i])
C[sy_i][sx_i] = 0

while len(Q) > 0:
    cost, y, x = Q.popleft()
    if C[y-1][x] == ".":
        Q.append([cost+1, y-1, x])
        C[y-1][x] = cost+1
    if C[y+1][x] == ".":
        Q.append([cost+1, y+1, x])
        C[y+1][x] = cost+1
    if C[y][x-1] == ".":
        Q.append([cost+1, y, x-1])
        C[y][x-1] = cost+1
    if C[y][x+1] == ".":
        Q.append([cost+1, y, x+1])
        C[y][x+1] = cost+1

print(C[gy_i][gx_i])