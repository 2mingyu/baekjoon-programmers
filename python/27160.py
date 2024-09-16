"""
할리갈리
"""
d = {'STRAWBERRY': 0,
     'BANANA': 0,
     'LIME': 0,
     'PLUM': 0}
N = int(input())
for _ in range(N):
    S, X = input().split()
    d[S] += int(X)
for i in d:
    if d[i] == 5:
        print('YES')
        exit()
print('NO')