"""
최소값 찾기
https://codio.tistory.com/entry/%EB%B0%B1%EC%A4%80-11003%EB%B2%88-%EC%B5%9C%EC%86%9F%EA%B0%92-%EC%B0%BE%EA%B8%B0-Python%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""
from collections import deque
N, L = map(int, input().split())
A = list(map(int, input().split()))
q = deque([(0, A[0])])
print(q[0][1], end=" ")
for i in range(1, N):
    if q and q[0][0] <= i-L:
        q.popleft()
    while q and A[i] <= q[-1][1]:
        q.pop()
    q.append((i, A[i]))
    print(q[0][1], end=" ")
