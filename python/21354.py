"""
Äpplen och päron
"""
A, P = map(int, input().split())
X = A*7 - P*13
print("lika" if not X else "Axel" if X>0 else "Petra")