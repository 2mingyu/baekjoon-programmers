"""
개표
"""
T = int(input())
for _ in range(T):
    n = int(input())
    s = '++++ ' * (n//5) + '|' * (n%5)
    print(s)