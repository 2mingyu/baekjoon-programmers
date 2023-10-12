"""
경로 찾기

플로이드-워셜 알고리즘 ??
"""
N = int(input())
edge = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            if edge[j][i] and edge[i][k]:
                edge[j][k] = 1
for e in edge:
    print(" ".join(map(str, e)))