"""
싱크홀

초기 수평 속력 V (단위 m/s)
구멍의 너비 W (단위 m)
벽에 닿을 때 까지 시간 t = W / V (단위 s)
벽에 닿을 때 까지 자유낙하 운동으로 이동한 거리 s = 5 * t ** 2 (단위 m)
"""
V, W, D = map(int, input().split())
r = 0
t = W / V
s = 5 * t ** 2
while s < D:
    r += 1
    # V *= 0.8
    # t = W / V
    t *= 1.25
    s += 5 * t ** 2
print(r)