"""
웜홀

다익스트라 알고리즘은 음수가 있으면 무한 루프에 빠질 수 있음
벨만-포드 알고리즘을 사용하자

도로는 양방향인데 계속 단방향으로 해서 틀림 ..
플로이드-워셜 알고리즘으로 풀리긴 함. PyPy3 로만 성공
graph[i][i] < 0 이 음수 사이클 확인
"""
import sys
input = sys.stdin.readline

def f():
    for k in range(N):
        for i in range(N):
            if k == i: continue
            for j in range(N):
                if k == j: continue
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                if graph[i][i] < 0: return 'YES'
    return 'NO'

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[500*2500*200*10000] * N for _ in range(N)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S-1][E-1] = min(graph[S-1][E-1], T)
        graph[E-1][S-1] = min(graph[E-1][S-1], T)
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S-1][E-1] = min(graph[S-1][E-1], -T)
    print(f())
