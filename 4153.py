"""
직각삼각형
"""
while True:
    l = list(map(int, input().split()))
    if sum(l) == 0: exit(0)
    Heru = max(l)
    l.remove(Heru)
    if Heru**2 == l[0]**2 + l[1]**2: print("right")
    else: print("wrong")