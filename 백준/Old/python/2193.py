"""
이친수

N = int(input())
from collections import deque
q = deque()
q.append('1')
count = 0
while q:
    pn = q.popleft()
    if len(pn) == N:
        count += 1
    else:
        if pn[-1] == '0':
            q.append(pn+'0')
            q.append(pn+'1')
        else:
            q.append(pn+'0')
print(count)

이건 메모리 초과
n번째 자리의 0의 개수 = n-1번째 자리의 0의 개수 + n-1번째 자리의 1의 개수
n번째 자리의 1의 개수 = n-1번째 자리의 0의 개수
최종 정답 = n번째 자리의 0의 개수 + n번째 자리의 1의 개수
"""
#N = int(input())
#s = [0, 1]
#for i in range(1,N): s = [s[0]+s[1], s[0]]
#print(s[0]+s[1])

a,b=0,1
for i in range(int(input())):a,b=a+b,a
print(a)