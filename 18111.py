"""
마인크래프트
256이 아니라 257을 넣어야 했어
"""
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
results = [N*M*2*257, 0]
for height in range(257):
    b1, b2 = 0, 0
    for n in range(N):
        for m in range(M):
            if land[n][m] > height:
                b1 += land[n][m] - height
            else :
                b2 += height - land[n][m]
    if b1 + B >= b2:
        t = b1*2 + b2
        if t <= results[0]:
            results = [t, height]
print(results[0], results[1])