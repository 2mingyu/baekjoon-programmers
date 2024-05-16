"""
Andando no tempo
"""
A, B, C = map(int, input().split())
print('S' if 1 in [A==B, A==C, B==C, A+B==C, A+C==B, A==B+C] else 'N')