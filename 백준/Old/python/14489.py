"""
치킨 두 마리 (...)
"""
A, B = map(int, input().split())
C = int(input())
r = A + B
if r >= C*2: print(r - C*2)
else: print(r)