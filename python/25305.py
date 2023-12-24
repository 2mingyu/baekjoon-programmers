"""
커트라인
"""
N, K = map(int, input().split())
x = sorted(list(map(int, input().split())), reverse=True)
print(x[K-1])