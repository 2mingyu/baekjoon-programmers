import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

for i in range(N):
    if a[i]:
        if i > 0 and a[i-1] == a[i]:
            print(-1)
            exit()
    else:
        l = a[i-1] if i > 0 else 0
        r = a[i+1] if i < N-1 else 0
        for c in (1, 2, 3):
            if c != l and c != r:
                a[i] = c
                break

print(*a)