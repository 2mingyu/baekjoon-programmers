x = 0
while True:
    x += 1
    n = int(input())
    if not n: break
    d = dict()
    for i in range(1, n+1):
        d[i] = {'name': input(), 'val': 0}
    for _ in range(2*n-1):
        a = int(input().split()[0])
        d[a]['val'] += 1
    for e in d:
        name, val = d[e]['name'], d[e]['val']
        if val != 2:
            print(x, name)