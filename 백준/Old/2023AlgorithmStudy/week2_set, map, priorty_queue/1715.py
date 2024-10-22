import sys
import heapq

N = int(input())
my_heap = []
for n in range(N):
    heapq.heappush(my_heap, int(sys.stdin.readline()))
result = 0
while len(my_heap) > 1:
    tmp1 = heapq.heappop(my_heap)
    tmp2 = heapq.heappop(my_heap)
    tmp3 = tmp1 + tmp2
    result = result + tmp3
    heapq.heappush(my_heap, tmp3)
print(result)
"""
작은 묶음부터 골라야지 비교가 적은 것을 확인
import itertools
N = 5
n_list_list = list(itertools.permutations(iterable=range(1, N+1), r=N))
for n_list in n_list_list:
    s = 0
    tmp = n_list[0]
    for n in n_list[1:]:
        print("(", tmp, "+", n, ")", end=" + ")
        s = s + tmp + n
        tmp = tmp + n
    print("\t= ", s)
"""