w, h = map(int, input().split())
n, a, b = map(int, input().split())
p = (w//a) * (h//b)
print(-1 if p == 0 else (n+p-1)//p)