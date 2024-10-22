"""
Pyramids
"""
while True:
    n = int(input())
    if not n: break
    print(sum([i for i in range(n+1)]))