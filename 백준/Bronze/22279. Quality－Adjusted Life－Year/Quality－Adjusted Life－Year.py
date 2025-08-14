N = int(input())
s = 0
for _ in range(N):
    q, y = map(float, input().split())
    s += q*y
print(s)