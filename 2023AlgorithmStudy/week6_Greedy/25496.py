"""
장신구 명장 임스
피로도 작은 것부터
"""
P, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
result = 0
while P < 200:
    if A:
        P += A.pop()
        result += 1
    else:
        break
print(result)