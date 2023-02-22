x, y = map(int, input().split())

abs_x, abs_y = abs(x), abs(y)
ans = 0

if abs_x > abs_y:
    ans += abs_x - abs_y
else:
    ans += abs_y - abs_x

if abs_x != x and abs_y != y:
    if abs_x > abs_y:
        pass
    elif abs_x < abs_y:
        ans += 2
elif abs_x != x:
    if abs_x > abs_y:
        ans += 1
    else:
        ans += 1
elif abs_y != y:
    if abs_x > abs_y:
        ans += 1
    else:
        ans += 1
else:
    if abs_x > abs_y:
        ans += 2
    elif abs_x < abs_y:
        pass

print(ans)