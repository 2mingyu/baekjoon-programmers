N = int(input())
l = list(map(int, input().split()))
for i in range(N):
    if l[i] % 2 == i%2:
        print('NO')
        exit()
print('YES')