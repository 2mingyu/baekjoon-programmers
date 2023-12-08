"""
바구니 뒤집기
"""
N, M = map(int, input().split())
B = [i for i in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    while i < j:
        B[i], B[j] = B[j], B[i]
        i += 1
        j -= 1
print(*B[1:])