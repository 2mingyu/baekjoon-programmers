"""
The Walking Adam
"""
T = int(input())
for _ in range(T):
    r = 0
    for c in input():
        if c == 'D': break
        r += 1
    print(r)