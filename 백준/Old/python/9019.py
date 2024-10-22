"""
DSLR

B가 1234라면, A를 최소한으로 우선 1234 2341 3412 4123로 변환?
set을 써서 같은지 확인? 은 아닌듯..
'가능한 명령어 나열이 여러가지면, 아무거나 출력한다.' -> LL = RR

set을 써서 중복된 n을 없앨 필요
문자열로 바꾸면 시간이 걸리기 때문에 정수로 연산
Python3로 계속 시간초과 나오다가 PyPy3로 하니까 됐다 ; ;
"""
from collections import*
for i in[*open(0)][1:]:
 n,B=map(int,i.split());t,q,s=1000,deque([(n,'')]),{n};h=t*10
 while n!=B:
  n,c=q.popleft()
  for i,j in zip([n*2%h,(n-1)%h,n%t*10+n//t,n%10*t+n//10],'DSLR'):
   if i not in s:s.add(i);q.append((i,c+j))
 print(c)