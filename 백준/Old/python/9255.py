"""
The Friend of My Enemy is My Enemy
"""
"""
K = int(input())
for x in range(K):
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(m)]
    s = int(input())
    r = set()
    for a in l:
        if a[0] == s: r.add(a[1])
        elif a[1] == s: r.add(a[0])
    print(f'Data Set {(x+1)}:')
    print(*sorted(r))
    print()
"""
"""
"""
p=print
for x in range(int(input())):
 n,m=map(int,input().split());l=[set()for _ in range(n+1)]
 for _ in range(m):a,b=map(int,input().split());l[a]|={b};l[b]|={a}
 p(f'Data Set {x+1}:');p(*sorted(l[int(input())]));p()
