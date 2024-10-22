"""
Máquina de café
"""
A = [int(input()) for _ in range(3)]
print(min(A[0]*4+A[1]*2, A[0]*2+A[2]*2, A[1]*2+A[2]*4))