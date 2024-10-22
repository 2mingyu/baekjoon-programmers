"""
Z
"""

N, r, c = map(int, input().split())
top, bottom, left, right = 0, 2**N - 1, 0, 2**N - 1
s, e = 0, (2**N)**2 - 1
while N > 1:
    row = (top + bottom) // 2
    col = (left + right) // 2
    d = (e-s+1) // 4
    if r <= row and c <= col:
        bottom, right = row, col
        s, e = s, s+d-1
    elif r <= row and c > col:
        bottom, left = row, col+1
        s, e = s+d, s+d+d-1
    elif r > row and c <= col:
        top, right = row+1, col
        s, e = s+d+d, s+d+d+d-1
    elif r > row and c > col:
        top, left = row+1, col+1
        s, e = s+d+d+d, s+d+d+d+d-1
    N -= 1
if r == top and c == left:
    print(s)
elif r == top and c == right:
    print(s+1)
elif r == bottom and c == left:
    print(s+2)
elif r == bottom and c == right:
    print(s+3)