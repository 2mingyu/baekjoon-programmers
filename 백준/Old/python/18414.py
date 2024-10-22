"""
X に最も近い値 (The Nearest Value)
"""
X, L, R = map(int, input().split())
if X < L: print(L)
elif X > R: print(R)
else: print(X)