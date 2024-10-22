"""
쉬움
"""
N = int(input())
rope = []
w = 0
for _ in range(N): rope.append(int(input()))
rope.sort()
k = N
for r in rope:
    w = max(w, r * k)
    k -= 1
print(w)