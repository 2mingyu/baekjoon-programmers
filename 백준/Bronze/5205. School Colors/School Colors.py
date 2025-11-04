K = int(input())
for x in range(1, K+1):
    n = int(input())
    s = [[]]
    for _ in range(n):
        s.append(list(map(int, input().split())))
    r = []
    m = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            t = (s[i][0]-s[j][0])**2 + (s[i][1]-s[j][1])**2 + (s[i][2]-s[j][2])**2
            if t > m:
                r = [[i, j]]
                m = t
            elif t == m:
                r.append([i, j])
    print(f'Data Set {x}:')
    for e in r: print(*e)