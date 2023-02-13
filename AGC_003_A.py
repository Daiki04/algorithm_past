S = list(input())
ans = [True, True]

if "N" in S and "S" not in S:
    ans[0] = False
if "S" in S and "N" not in S:
    ans[0] = False
if "E" in S and "W" not in S:
    ans[1] = False
if "W" in S and "E" not in S:
    ans[1] = False

print("Yes" if all(ans) else "No")