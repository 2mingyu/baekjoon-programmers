"""
Do Not Touch Anything
"""
R, C, N = map(int,input().split())
print((C//N + bool(C%N)) * (R//N + bool(R%N)))