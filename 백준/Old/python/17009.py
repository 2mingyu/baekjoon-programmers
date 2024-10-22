"""
Winning Score
"""
A = int(input()) * 3 + int(input()) * 2 + int(input())
B = int(input()) * 3 + int(input()) * 2 + int(input())
if A > B: print('A')
elif A == B: print('T')
else: print('B')