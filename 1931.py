"""
회의실 배정
남은 가능한 회의 중에서 가장 빨리 끝나는 회의를 선택 하면 될듯?
"""
from collections import deque
l = []
for _ in range(int(input())):l.append(list(map(int,input().split())))
q=deque(sorted(l,key=lambda x:(x[1],x[0])))
c=1
t=q.popleft()[1]
while q:
    s,e=q.popleft()
    if t<=s:
        t=e
        c+=1
print(c)