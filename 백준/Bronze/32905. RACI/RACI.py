n, m = map(int, input().split())
for _ in range(n):
    if input().count('A') != 1:
        print('No')
        exit()
print('Yes')