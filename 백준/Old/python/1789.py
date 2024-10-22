"""
수들의 합
1 = 1
2 = 2
3 = 1+2
4 = 1+3
5 = 2+3
6 = 1+2+3
10 = 1+2+3+4
15 = 1+2+3+4+5
"""
S = int(input())
t = 0
N = 0
while True:
    N += 1
    t += N
    if t > S: break
print(N-1)