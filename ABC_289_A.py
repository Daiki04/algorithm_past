s = list(input())

s_reverse = ["1" if i == "0" else "0" for i in s]

print("".join(s_reverse))