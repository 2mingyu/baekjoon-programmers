"""
시험 감독

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
r = 0
for i in range(N):
    A[i] -= B
    r += 1
    if A[i] > 0:
        r += A[i]//C + (A[i]%C > 0)
print(r)
"""
r=int(input())
A=list(map(int,input().split()))
B,C=map(int,input().split())
for a in A:
 a-=B
 if a>0:r+=a//C+(a%C>0)
print(r)