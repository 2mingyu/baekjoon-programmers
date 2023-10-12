import sys
import heapq

N = int(input())
my_heap = []
results = []
for n in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if my_heap:
            # 실제 원소 값은 튜플의 두 번째 자리에 저장되어 있으므로 [1] 인덱싱을 통해 접근
            results.append(heapq.heappop(my_heap)[1])
        else:
            results.append(0)
    else:
        # 힙에 원소를 추가할 때 (-item, item)의 튜플 형태로 넣어주면 튜플의 첫 번째 원소를 우선순위로 힙을 구성하게 된다.
        heapq.heappush(my_heap, (abs(tmp), tmp))
for r in results:
    print(r)