"""
덱

sys.stdin.readline 안쓰면 시간 초과
"""
import sys
from collections import deque
q = deque()
for _ in range(int(input())):
    c = sys.stdin.readline().split()
    if c[0] == 'push_front':
        q.appendleft(int(c[1]))
    elif c[0] == 'push_back':
        q.append(int(c[1]))
    elif c[0] == 'pop_front':
        if q: print(q.popleft())
        else: print(-1)
    elif c[0] == 'pop_back':
        if q: print(q.pop())
        else: print(-1)
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        print(int(not q))
    elif c[0] == 'front':
        if q: print(q[0])
        else: print(-1)
    elif c[0] == 'back':
        if q: print(q[-1])
        else: print(-1)