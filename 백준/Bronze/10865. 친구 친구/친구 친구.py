import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    cnt[A] += 1
    cnt[B] += 1
for i in range(1, N + 1):
    print(cnt[i])