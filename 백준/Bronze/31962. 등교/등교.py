N, X = map(int, input().split())
r = -1
for _ in range(N):
    S, T = map(int, input().split())
    if S + T <= X:
        r = max(r, S)
print(r)