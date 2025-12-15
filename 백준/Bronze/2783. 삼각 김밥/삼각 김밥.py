X, Y = map(int, input().split())
t = X/Y*1000
N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    t = min(t, X/Y*1000)
print(t)