import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    m = int(input())
    l = [list(map(int, input().split())) for _ in range(m)]
    l.sort(key=lambda x: (x[0], x[2]))
    r = 0
    d = 0
    e = 0
    for x in l:
        if x[0] > d:
            e = 0
            d = x[0]
        if e <= x[1]:
            e = x[2]
            r += 1
    print(f"Scenario #{i+1}:\n{r}\n")