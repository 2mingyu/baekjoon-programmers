"""
Pizza Deal
"""
import math
A, P1 = map(int, input().split())
R, P2 = map(int, input().split())
print('Whole pizza' if A/P1 < (R*R*math.pi)/P2 else 'Slice of pizza')