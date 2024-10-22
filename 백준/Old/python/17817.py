"""
Trol

0 1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9 1
2 3 4 5 6 7 8 9 1 2
3 4 5 6 7 8 9 1 2 3
4 5 6 7 8 9 1 2 3 4
5 6 7 8 9

99: 9
100: 1
101: 2
999: 9
1000: 1

A = N % 9
if A == 0: A = 9

A = N%9 or 9

이 아래 코드는 당연히 시간초과 나오겠지
A = l%9 or 9
s = 0
for i in range(l, r+1):
    s += A
    A += 1
    if A == 10: A = 1
print(s)
"""
f=lambda x:x//9*45+x%9*(x%9+1)//2
for _ in ' '*int(input()):l,r=map(int,input().split());print(f(r)-f(l-1))
