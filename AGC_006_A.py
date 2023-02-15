N = int(input())
s = input()
t = input()
ans = ""

if s == t:
    print(len(s))
else:
    for i in range(N):
        if s[i:] == t[:N-i]:
            ans = s[:i] + t
            break
        if i == N-1:
            ans = s + t
        
    print(len(ans))