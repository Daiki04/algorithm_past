N, M = map(int, input().split())

num_dic = {i: [] for i in range(1, N+1)}
connected_components = []
    
for _ in range(M):
    x, y = map(int, input().split())
    for i in connected_components:
        if x in i or y in i:
            i.add(x)
            i.add(y)
            break
    else:
        connected_components.append({x, y})         

flag = True
while flag:
    flag = False
    for i in range(len(connected_components)):
        if i == set():
            continue
        for j in range(i+1, len(connected_components)):
                if connected_components[i] & connected_components[j]:
                    flag = True
                    connected_components[i] |= connected_components[j]
                    connected_components[j] = set()

for i in range(1, N+1):
    flag = True
    for j in connected_components:
        if i in j:
            flag = False
            break
    if flag:
        connected_components.append({i})

ans = 0

for i in connected_components:
    if i != set():
        ans += 1

print(ans)