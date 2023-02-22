a, b, x = map(int, input().split())

s = a // x
if a % x != 0:
    s += 1

e = b // x

print(e - s + 1)