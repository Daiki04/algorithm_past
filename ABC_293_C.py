H, W = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(H)]

task = [(0, 1), (1, 0)]
ans = 0

hist = []

def dfs(x, y, hist):
    global ans
    for dx, dy in task:
        if 0 <= x+dx < H and 0 <= y+dy < W and G[x+dx][y+dy] not in hist:
            dfs(x+dx, y+dy, hist+[G[x+dx][y+dy]])
    if x == H-1 and y == W-1:
        ans += 1

dfs(0, 0, [G[0][0]])

print(ans)
        