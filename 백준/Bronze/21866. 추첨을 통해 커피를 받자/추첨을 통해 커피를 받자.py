a = list(map(int, input().split()))
b = [100, 100, 200, 200, 300, 300, 400, 400, 500]
for i in range(9):
    if a[i] > b[i]:
        print('hacker')
        exit()
if sum(a) < 100: print('none')
else: print('draw')