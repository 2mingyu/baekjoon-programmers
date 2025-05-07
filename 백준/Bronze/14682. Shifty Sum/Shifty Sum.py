N = int(input())
k = int(input())
s = N
for _ in range(k):
    N *= 10
    s += N
print(s)