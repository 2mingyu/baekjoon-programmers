l = int(input())
N = int(input())
t = float(input())
for _ in range(N):
    f, b = map(float, input().split())
    if l/f + l/b < t:
        print('HOPE')
        exit()
print('DOOMED')