s = list(input())
K = int(input())
base = ord("a")
last = ord("z")

for i in range(len(s)):
    if s[i] == "a":
        continue
    if K >= last - ord(s[i]) + 1:
        K -= last - ord(s[i]) + 1
        s[i] = "a"

if K > 0:
    s[-1] = chr(ord(s[-1]) + K % 26)
print("".join(s))