r = 0
for _ in range(4) :
    l, x = input().split()
    r += int(x) * [21, 17][l =='Stair']
print(r)