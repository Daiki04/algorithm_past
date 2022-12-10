S = input()

na, nb, nc = S.count("a"), S.count("b"), S.count("c")

max_abc = max(na, nb, nc)

if na == max_abc:
    print("a")
if nb == max_abc:
    print("b")
if nc == max_abc:
    print("c")