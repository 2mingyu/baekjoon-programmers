"""
숨바꼭질 2
"""
from collections import deque
N, K = map(int, input().split())
if N == K:
    print(0)
    print(1)
else:
    visited = [-1] * 100001
    q = deque()
    visited[N] = 0
    q.append(N)
    fastestNum = 0
    while q:
        location = q.popleft()
        if location == K:
            fastestNum += 1
            continue
        for next_location in location-1, location+1, location*2:
            if 0 <= next_location <= 100000 and (visited[next_location] == visited[location]+1 or visited[next_location] == -1):
                visited[next_location] = visited[location] + 1
                q.append(next_location)
    print(visited[K])
    print(fastestNum)