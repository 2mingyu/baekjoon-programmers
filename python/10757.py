"""
큰 수 A+B
"""
A,B=map(list,input().split())
C=''
n=0
while A or B:
    if A:n+=int(A.pop())
    if B:n+=int(B.pop())
    C+=str(n)[-1]
    n//=10
if n:print('1',end="")
print(C[::-1])