"""
가장 가까운 세 사람의 심리적 거리
N >= 33 일 경우 무조건 0이라고 해줘야 시간초과 피함
"""
import sys
input = sys.stdin.readline
for _ in range(int(input().strip())):
    N = int(input().strip())
    s = input().split()
    if N >= 33:
        print(0)
        continue
    r = N * 3 * 4
    for p1 in range(N-2):
        for p2 in range(p1+1, N-1):
            for p3 in range(p2+1, N):
                score = 0
                for i in 0,1,2,3:
                    if s[p1][i] != s[p2][i]: score += 1
                    if s[p1][i] != s[p3][i]: score += 1
                    if s[p2][i] != s[p3][i]: score += 1
                r = min(r, score)
    print(r)