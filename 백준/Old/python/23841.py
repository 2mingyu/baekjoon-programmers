"""
데칼코마니

INU 코드페스티벌 2021 A
"""
N, M = map(int, input().split())
for _ in range(N):
    old = input()
    new = ''
    for i in range(M//2):
        c = '.'
        if old[i] != '.': c = old[i]
        elif old[M-1-i] != '.': c = old[M-1-i]
        new += c
    print(new+new[::-1])