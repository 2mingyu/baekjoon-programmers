"""
이중 우선순위 큐
heappush 하면 맨 앞 원소는 최소값으로 보장됨
https://hongcoding.tistory.com/92

import heapq
import sys
input = sys.stdin.readline
for i in range(int(input())):
    k = int(input())
    min_heap, max_heap = [], []
    visited = [False] * k
    for j in range(k):
        c, n = input().split()
        n = int(n)
        if c == 'I':
            heapq.heappush(min_heap, (n, j))
            heapq.heappush(max_heap, (-n, j))
            visited[j] = True
        else:
            if n == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    if not max_heap or not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])

dict() 쓰니까 시간초과나네
dict()가 아니라 sys.stdin.readline 문제였던듯
심지어 dict()가 더 빠르고 메모리 적게 씀 !
"""
import heapq
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    max_heap = []
    min_heap = []
    d = dict()
    for _ in range(int(input())):
        c, n = input().split()
        n = int(n)
        if c == 'I':
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, n)
            if n not in d: d[n] = 1
            else: d[n] += 1
        else:
            if n == 1:
                while max_heap and d[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    d[-max_heap[0]] -= 1
                    heapq.heappop(max_heap)
            else:
                while min_heap and d[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    d[min_heap[0]] -= 1
                    heapq.heappop(min_heap)
    while max_heap and d[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and d[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    if not max_heap:
        print("EMPTY")
    else:
        print(-heapq.heappop(max_heap), heapq.heappop(min_heap))