"""
부당한 퍼즐
"""
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
t = b.index(a[0])
if a == b[t::-1]+b[-1:t:-1] or a == b[t:] + b[:t]:
    print('good puzzle')
else:
    print('bad puzzle')