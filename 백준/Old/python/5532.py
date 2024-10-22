"""
방학 숙제
"""
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
a = A // C
if A % C: a += 1
b = B // D
if B % D: b += 1
print(L - max(a, b))