x, y, z = map(int, input().split())
x_, y_, z_ = map(int, input().split())
if y_ >= (y+1)//2:
    if y_ >= y:
        if x_ >= (x+1)//2:
            if x_ >= x:
                print('A')
            else:
                print('B')
        else:
            print('C')
    else:
        print('D')
else:
    print('E')