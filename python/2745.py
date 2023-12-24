"""
진법 변환
"""
N, B = input().split()
N = N[::-1]
B = int(B)
r = 0
for i in range(len(N)):
    if N[i] in '0123456789': n = int(N[i])
    else: n = ord(N[i]) - 55
    r += (B**i) * n
print(r)