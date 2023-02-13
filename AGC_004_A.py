A, B, C = map(int, input().split())
Blocks = [A, B, C]

for i in range(3):
    l1 = Blocks[i] // 2
    l2 = Blocks[i] - l1

    if l1 == 0 or l2 == 0:
        continue

    if i == 0:
        ans = abs(l1*Blocks[(i+1)%3]*Blocks[(i+2)%3]-l2*Blocks[(i+1)%3]*Blocks[(i+2)%3])
        continue
    ans = min(ans, abs(l1*Blocks[(i+1)%3]*Blocks[(i+2)%3]-l2*Blocks[(i+1)%3]*Blocks[(i+2)%3]))

print(ans)