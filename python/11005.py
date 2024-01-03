"""
진법 변환 2
"""
N, B = map(int, input().split())
r = ''
while N:
    r += str('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[N%B])
    N //= B
print(r[::-1])