n, k = map(int, input().split())
s = sum([int(input()) for _ in range(k)])
r = n-k
a = (s-3*r)/n
b = (s+3*r)/n
print(a, b)