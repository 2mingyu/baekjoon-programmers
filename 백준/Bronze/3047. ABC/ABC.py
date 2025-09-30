A, B, C = sorted(map(int, input().split()))
for c in input():
    if c == 'A': print(A, end=' ')
    elif c == 'B': print(B, end=' ')
    else: print(C, end=' ')