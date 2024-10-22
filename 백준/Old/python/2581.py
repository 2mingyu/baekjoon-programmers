"""
소수
"""
M=int(input())
N=int(input())
p=[0,0]+[1]*(N-1)
for i in range(2,N+1):
    ii=i*2
    while ii<=N:
        p[ii]=0
        ii+=i
s=m=0
for i in range(N,M-1,-1):
    if p[i]:
        s+=i
        m=i
if m:
    print(s)
    print(m)
else: print(-1)