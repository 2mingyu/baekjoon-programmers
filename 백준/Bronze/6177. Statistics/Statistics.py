N = int(input())
X = sorted([int(input()) for _ in range(N)])
print(sum(X)/N)
print(X[N//2] if N%2 else (X[N//2-1]+X[N//2])/2)