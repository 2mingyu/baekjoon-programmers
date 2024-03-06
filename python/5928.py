"""
Contest Timing
"""
D, H, M = map(int, input().split())
t = (D-11) * 24 * 60 + (H-11) * 60 + (M-11)
if t < 0: print(-1)
else: print(t)