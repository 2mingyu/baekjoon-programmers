"""
뱀과 사다리 게임
"""
from collections import deque
N, M = map(int, input().split())
ladders = [list(map(int, input().split())) for _ in range(N)]
snakes = [list(map(int, input().split())) for _ in range(M)]
visited = [True]*2 + [False]*99
q = deque([(1, 0)])
while q:
    position, count = q.popleft()
    for i in 1,2,3,4,5,6:
        next_position = position+i
        for ladder in ladders:
            if ladder[0] == next_position:
                next_position = ladder[1]
                break
        for snake in snakes:
            if snake[0] == next_position:
                next_position = snake[1]
                break
        if not visited[next_position]:
            visited[next_position] = True
            q.append((next_position, count+1))
        if next_position == 100:
            print(count+1)
            exit()