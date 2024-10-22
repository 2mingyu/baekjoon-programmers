"""
고양이 카페
두 무게 더한 값이 최대한 K와 가깝게?
"""
N, K = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
i = 0
ii = N - 1
result = 0
while i < ii:
    if w[i] + w[ii] <= K:
        i += 1
        ii -= 1
        result += 1
    else:
        ii -= 1
print(result)