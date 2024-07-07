"""
금메달, 은메달, 동메달은 누가?
"""
N, M = map(int, input().split())
a = []
for i in range(1, N+1):
    j = int(input())
    a = a[:j-1] + [i] + a[j-1:]

b = []
for i in a[M-1::-1]:
    j = int(input())
    b = b[:j-1] + [i] + b[j-1:]

for i in range(3):
    print(b[i])