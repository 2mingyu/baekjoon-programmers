r = 0
n, m = map(int, input().split())
v = [False]*10
if m:
    for i in map(int, input().split()): v[i] = True

def f(d, c):
    global r
    if d == n:
        if c == m:
            r += 1
        return
    for i in range(10):
        if v[i]:
            v[i] = False
            f(d+1, c+1)
            v[i] = True
        else:
            f(d+1, c)

f(0, 0)
print(r)