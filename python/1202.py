"""
보석 도둑

jewel을 sort 하면, 0번 인덱스(무게)에 대해 오름차순 정렬, 무게가 같으면 1번 인덱스(가격)에 대해 오름차순 정렬
우선순위큐 (pq) 에는, 현재 가방에 들어갈 수 있는 무게의 보석들의 가격이 들어있음
heapq는 최소 힙이니까 가격을 음수로 넣어야 최대 힙이 됨.
"""
import sys
import heapq
from collections import deque
input = sys.stdin. readline

N, K = map(int, input().split())
jewel = deque(sorted([list(map(int, input().split())) for _ in range(N)]))
bag = sorted([int(input()) for _ in range(K)])
pq = []
r = 0

for b in bag:
    while jewel:
        if jewel[0][0] <= b:
            heapq.heappush(pq, -jewel.popleft()[1])
        else:
            break
    if pq:
        r += -heapq.heappop(pq)

print(r)