"""
Polynesiaglot (Large)

뒤에서 부터 채운다고 생각하면?
모음 부터 시작, 자음 바로 뒤에는 모음이 오도록
c: 끝 자리가 자음
v: 끝 자리가 모음

숏코딩

for x in range(int(input())):
 C,V,L=map(int,input().split())
 c,v=0,V
 for _ in range(L-1):c,v=v*C,(c+v)*V
 print(f'Case #{x+1}: {(c+v)%(10**9+7)}')
"""
m = 10**9 + 7
T = int(input())
for x in range(1, T+1):
    C, V, L = map(int, input().split())
    c, v = 0, V
    for _ in range(L-1):
        c, v = v * C, (c+v) * V
    print(f'Case #{x}: {(c+v)%m}')