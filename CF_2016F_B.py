N = int(input())

total = 0
ans = []

for i in range(1, N+1):
    if total >= N:
        break

    ans.append(i)
    total += i

delta = total - N
if delta != 0:
    ans.remove(delta)
for i in ans :
    print(i)