import sys
import heapq

N = int(input())
my_heap = []
results = []
for n in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if my_heap:
            results.append(heapq.heappop(my_heap))
        else:
            results.append(0)
    else:
        heapq.heappush(my_heap, tmp)
for r in results:
    print(r)