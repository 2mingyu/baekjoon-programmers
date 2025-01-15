import heapq

N = int(input())
l = sorted([list(map(int, input().split())) for _ in range(N)])
q = []
heapq.heappush(q, l[0][1])
for i in range(1, N):
    if q[0] <= l[i][0]:
        heapq.heappushpop(q, l[i][1])
    else:
        heapq.heappush(q, l[i][1])
print(len(q))