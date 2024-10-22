T = int(input())
results = []
for t in range(T):
    results.append(0)
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    n = 0
    index_B = 0
    while n < N:
        while index_B < M:
            if A[n] > B[index_B]:
                index_B += 1
            else:
                break
        results[t] += index_B
        n += 1
for r in results:
    print(r)