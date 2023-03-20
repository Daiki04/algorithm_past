N, M = map(int, input().split())

cells = [{"R": -1, "B": -1} for _ in range(N)]

for _ in range(M):
    a, b, c, d = input().split()
    a, c = int(a)-1, int(c)-1

    if cells[a][b] == -1 and cells[c][d] == -1:
        cells[a][b] = c
        cells[c][d] = a

flag = [False] * N
ans = 0

def dfs(i, last, start):
    global flag
    global ans
    
    for j in cells[i].values():
        if j != -1 and j != last and j != start:
            flag[j] = True
            dfs(j, i, start)
    
    for j in cells[i].values():
        if j != -1 and j != last and j == start:
            ans += 1
    
    if last == start and cells[i]["R"] == start and cells[i]["B"] == start:
        ans += 1

s = 0
for i in range(N):
    if not flag[i]:
        s += 1
        dfs(i, -1, i)

print(ans, s-ans)