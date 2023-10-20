"""
연구소

벽 세우기는 모든 경우 해보기?
바이러스 퍼지는 건 bfs

세울 벽이 3개니까 i, j, k로 반복문 쓰는데, 세울 벽이 많아지면 재귀 해야할 듯
nl을 visited 대신 쓸 수도 있네
"""
from collections import deque
import copy
def bfs(nl):
    q = deque(virus)
    while q:
        v = q.popleft()
        if v-M >= 0 and nl[v-M] == 0:
            nl[v-M] = 2
            q.append(v-M)
        if v-1 >= 0 and (v-1) % M != M-1 and nl[v-1] == 0:
            nl[v-1] = 2
            q.append(v-1)
        if v+M < N*M and nl[v+M] == 0:
            nl[v+M] = 2
            q.append(v+M)
        if v+1 < N*M and (v+1) % M != 0 and nl[v+1] == 0:
            nl[v+1] = 2
            q.append(v+1)
    return nl.count(0)

N, M = map(int,input().split())
l = []
for _ in range(N): l += list(map(int, input().split()))

virus = []
for i in range(N*M):
    if l[i] == 2: virus.append(i)

r = 0
for i in range(N*M-2):
    if l[i] == 0:
        for j in range(i+1, N*M-1):
            if l[j] == 0:
                for k in range(j+1, N*M):
                    if l[k] == 0:
                        nl = copy.deepcopy(l)
                        nl[i] = nl[j] = nl[k] = 1
                        r = max(r, bfs(nl))

print(r)