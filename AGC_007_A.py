H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]
sharp_counts = 0
actions = [(1, 0), (0, 1)]

for i in range(H):
    for j in range(W):
        if G[i][j] == "#":
            sharp_counts += 1

sx, sy = 0, 0
gx, gy = H-1, W-1

def dfs(x, y, c):
    c += 1
    if x == gx and y == gy and sharp_counts == c:
        print("Possible")
        exit()
    
    for dx, dy in actions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and G[nx][ny] == "#":
            dfs(nx, ny, c)

dfs(sx, sy, 0)
print("Impossible")