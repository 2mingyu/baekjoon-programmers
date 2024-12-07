n, d = map(int, input().split())
l = []
s = 0
for _ in range(n):
    t = int(input())
    l.append(t)
    s += t
for e in l:
    print(d*e//s)