"""
오 이거 운영체제 SJF 아닌가
시간 짧은 사람이 앞으로.
"""
N = int(input())
P = list(map(int, input().split()))
P.sort()
i = N
s = 0
for p in P:
    s += p * i
    i -= 1
print(s)