import sys
sys.setrecursionlimit(1000000)

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
s = [0, 0]
e = [0, 0]
flag = [[False] * W for _ in range(H)]

for i in range(H):
    c = C[i]
    if "s" in c:
        for j in range(W):
            if c[j] == "s":
                s = [i, j]
    if "g" in c:
        for j in range(W):
            if c[j] == "g":
                e = [i, j]

def dfs(point):
    flag[point[0]][point[1]] = True

    for p in [[point[0]-1, point[1]], [point[0]+1, point[1]], [point[0], point[1]-1], [point[0], point[1]+1]]:
        if 0<=p[0]<H and 0<=p[1]<W and C[p[0]][p[1]] != "#" and not flag[p[0]][p[1]]:
            dfs(p)

dfs(s)

if flag[e[0]][e[1]]:
    print("Yes")
else:
    print("No")