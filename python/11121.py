"""
Communication Channels
"""
T = int(input())
for _ in range(T):
    a, b = input().split()
    print(['ERROR', 'OK'][a == b])