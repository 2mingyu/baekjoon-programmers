n = int(input())
for _ in range(n):
    s, i, j = input().split()
    print(s[:int(i)] + s[int(j):])