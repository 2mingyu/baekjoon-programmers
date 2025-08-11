NR, NC = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(NR)]
s = 0
r = c = 0
for i in range(1, NR-1):
    for j in range(1, NC-1):
        t = 0
        for tr in range(i-1, i+2):
            for tc in range(j-1, j+2):
                t += m[tr][tc]
        if t > s:
            s = t
            r, c = i, j
print(s)
print(r, c)