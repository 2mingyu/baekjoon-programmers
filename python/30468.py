"""
호빈우가 학교에 지각한 이유 1
"""
S, D, I, L, N = map(int, input().split())
print(max(N*4 - sum([S, D, I, L]), 0))