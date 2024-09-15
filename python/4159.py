"""
알래스카
"""
def f():
    for i in range(1, n):
        if l[i] - l[i-1] > 200:
            print('IMPOSSIBLE')
            return
    if (1422-l[-1])*2 > 200:
        print('IMPOSSIBLE')
        return
    print('POSSIBLE')

while True:
    n = int(input())
    if n == 0: break
    l = sorted([int(input()) for _ in range(n)])
    f()