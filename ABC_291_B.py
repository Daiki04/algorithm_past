N = int(input())
X = list(map(int, input().split()))
X.sort()

X = X[N:]

X.sort(reverse=True)

X = X[N:]


print(sum(X) / (3*N) )