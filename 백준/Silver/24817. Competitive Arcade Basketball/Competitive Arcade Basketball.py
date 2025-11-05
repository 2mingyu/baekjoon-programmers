import sys
input = sys.stdin.readline

n, p, m = map(int, input().split())
d = {input().strip(): 0 for _ in range(n)}
c = False
for _ in range(m):
    a, b = input().split()
    d[a] += int(b)
    if d[a] >= p:
        print(a, 'wins!')
        d[a] = -float('inf')
        c = True
if not c: print('No winner!')