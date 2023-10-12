"""
손익분기점
"""
A, B, C = map(int, input().split())
if C > B: print(A//(C-B) + 1)
else: print(-1)