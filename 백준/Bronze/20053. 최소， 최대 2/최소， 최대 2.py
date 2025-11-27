T = int(input())
for _ in range(T):
    N = int(input())
    a = -float('inf')
    b = float('inf')
    for x in map(int, input().split()):
        if x > a:
            a = x
        if x < b:
            b = x
    print(b, a)