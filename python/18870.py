"""
좌표 압축
"""
N = int(input())
X = list(map(int, input().split()))
sorted_X = list(sorted(set(X)))
d = dict()
for i in range(len(sorted_X)):
    d[sorted_X[i]] = i
for x in X:
    print(d[x], end=' ')