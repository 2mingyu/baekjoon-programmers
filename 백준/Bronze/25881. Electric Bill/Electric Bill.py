a, b = map(int, input().split())
n = int(input())
for _ in range(n):
    c = int(input())
    print(c, a*min(1000, c) + b*max(0, c-1000))