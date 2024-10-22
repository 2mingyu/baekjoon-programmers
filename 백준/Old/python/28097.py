"""
모범생 포닉스
"""
N = int(input())
T = input().split()
x = (len(T)-1) * 8
for t in T: x += int(t)
print(x//24, x%24)