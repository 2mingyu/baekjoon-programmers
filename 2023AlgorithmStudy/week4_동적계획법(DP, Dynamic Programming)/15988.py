"""
1: 1 (1)
2: 2 (1+1, 2)
3: 4 (1+1+1, 1+2, 2+1, 3)
4: 7 (...)
5: 13 (1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1, 1+1+3, 1+3+1, 3+1+1, 2+3, 3+2)

??? s[n] = s[n-1] + s[n-2] + s[n-3] ???
"""
import sys

T = int(input())
s = [0, 1, 2, 4]    # s[n]은 n을 1,2,3의 합으로 나타내는 방법의 수
results = []
for _ in range(T):
    n = int(sys.stdin.readline())
    for i in range(len(s), n+1):
        s.append((s[i-1] + s[i-2] + s[i-3]) % 1000000009)
    results.append(s[n])
for r in results:
    print(r)