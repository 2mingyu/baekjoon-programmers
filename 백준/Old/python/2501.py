"""
약수 구하기
"""
N, K = map(int, input().split())
i = 0
for q in range(1, N+1):
    if N % q == 0:
        i += 1
        if i == K:
            print(q)
            exit(0)
print(0)