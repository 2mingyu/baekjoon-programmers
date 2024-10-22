"""
준영이의 등급
"""
N, K = map(int, input().split())
G = list(map(int, input().split()))
D = []
for g in G:
    P = g * 100 // N
    if P <= 4: D.append(1)
    elif P <= 11: D.append(2)
    elif P <= 23: D.append(3)
    elif P <= 40: D.append(4)
    elif P <= 60: D.append(5)
    elif P <= 77: D.append(6)
    elif P <= 89: D.append(7)
    elif P <= 96: D.append(8)
    else: D.append(9)
print(*D)