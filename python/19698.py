"""
헛간 청약
"""
N, W, H, L = map(int, input().split())
print(min(N, (W//L)*(H//L)))