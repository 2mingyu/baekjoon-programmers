"""
지능형 기차
"""
m, c = 0, 0
for i in range(4):
    a, b = map(int, input().split())
    c = c - a + b
    m = max(m, c)
print(m)