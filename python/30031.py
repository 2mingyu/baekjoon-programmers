"""
지폐 세기
"""
N = int(input())
r = 0
d = {'136': 1000, '142': 5000, '148': 10000, '154': 50000}
for _ in range(N): r += d[input().split()[0]]
print(r)