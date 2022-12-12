N = int(input())
digit = N // 9 + 1
num = N % 9
ans = 0

if num == 0:
    digit -= 1
    num = 9

for i in range(digit):
    ans += num * (10**i)

print(ans)