"""
테트로미노

현재 위치를 (y,x)

y,x  y,x+1  y,x+2  y,x+3        ㅡ
y,x  y+1,x  y+2,x  y+3,x        ㅣ

y,x  y+1,x  y,x+1  y+1,x+1      ㅁ


y,x  y,x+1  y,x+2  y+1,x+1       ㅜ
y,x  y+1,x  y+2,x  y+1,x+1       ㅏ
y+1,x  y,x+1  y+1,x+1  y+2,x+1  ㅓ
y,x+1  y+1,x+1  y+1,x  y+1,x+2  ㅗ

y,x  y+1,x  y+1,x+1  y+2,x+1
y,x  y,x+1  y+1,x+1  y+1,x+2
y+1,x  y+1,x+1  y,x+1  y,x+2
y,x+1  y+1,x+1  y+1,x  y+2,x

y,x  y+1,x  y+2,x  y+2,x+1      ㄴ
y,x  y+1,x  y+1,x+1  y+1,x+2    ㄴ
y,x  y,x+1  y,x+2  y+1,x+2      ㄱ
y,x  y,x+1  y+1,x+1  y+2,x+1    ㄱ
y+1,x  y+1,x+1  y+1,x+2  y,x+2  ㅢ
y+2,x  y+2,x+1  y+1,x+1  y,x+1  ㅢ
y,x  y+1,x  y,x+1  y,x+2
y,x  y,x+1  y+1,x  y+2,x
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = []
r = 0
for _ in range(N): l.append(list(map(int, input().split())))
for y in range(N):
    for x in range(M):
        shapeList = [
            [[y,x], [y,x+1], [y,x+2], [y,x+3]],
            [[y,x], [y+1,x], [y+2,x], [y+3,x]],
            [[y,x], [y+1,x], [y,x+1], [y+1,x+1]],
            [[y,x], [y,x+1], [y,x+2], [y+1,x+1]],
            [[y,x], [y+1,x], [y+2,x], [y+1,x+1]],
            [[y+1,x], [y,x+1], [y+1,x+1], [y+2,x+1]],
            [[y,x+1], [y+1,x+1], [y+1,x], [y+1,x+2]],
            [[y,x], [y+1,x], [y+1,x+1], [y+2,x+1]],
            [[y,x], [y,x+1], [y+1,x+1], [y+1,x+2]],
            [[y+1,x], [y+1,x+1], [y,x+1], [y,x+2]],
            [[y,x+1], [y+1,x+1], [y+1,x], [y+2,x]],
            [[y,x], [y+1,x], [y+2,x], [y+2,x+1]],
            [[y,x], [y+1,x], [y+1,x+1], [y+1,x+2]],
            [[y,x], [y,x+1], [y,x+2], [y+1,x+2]],
            [[y,x], [y,x+1], [y+1,x+1], [y+2,x+1]],
            [[y+1,x], [y+1,x+1], [y+1,x+2], [y,x+2]],
            [[y+2,x], [y+2,x+1], [y+1,x+1], [y,x+1]],
            [[y,x], [y+1,x], [y,x+1], [y,x+2]],
            [[y,x], [y,x+1], [y+1,x], [y+2,x]]
        ]
        for shape in shapeList:
            condition = True
            s = 0
            for square in shape:
                if square[0] >= N or square[1] >= M:
                    condition = False
                    break
                else:
                    s += l[square[0]][square[1]]
            if condition:
                r = max(r, s)
print(r)