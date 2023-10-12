"""
달팽이는 올라가고 싶다
d, h = 0, 0 으로 하면 시간이 오래 걸려서, 초기값을 정답 근처로 넣어줌
숏코딩 보니까 1 - (A-V)//(A-B) 가 답이래
"""
A, B, V = map(int, input().split())
d = (V-A) // (A-B)
h = d * (A-B)
while True:
    h += A
    d += 1
    if h >= V: break
    h -= B
print(d)