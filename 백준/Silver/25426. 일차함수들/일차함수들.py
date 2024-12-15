N = int(input())
a = []
b = []
x = []
for i in range(N):
    x.append(i+1)
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
x.sort()
a.sort()
r = 0
for i in range(N):
    r += a[i]*x[i] + b[i]
print(r)