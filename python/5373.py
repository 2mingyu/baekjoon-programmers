"""
큐빙

위 U white
아래 D yellow
앞 F red
뒤 B orange
왼 L green
오 R blue

           B
         8 7 6
         5 4 3
         2 1 0

  6 3 0  0 1 2  2 5 8          6 7 8
L 7 4 1  3 4 5  1 4 7 R        3 4 5
  8 5 2  6 7 8  0 3 6          0 1 2

         0 1 2
         3 4 5
         6 7 8
           F
"""
import sys
input = sys.stdin.readline
def rotate(x, y):
    if x == 'U':
        h = 'BRFL'
        i = [[2,1,0],[2,1,0],[2,1,0],[2,1,0]]
    elif x == 'D':
        h = 'FRBL'
        i = [[6,7,8],[6,7,8],[6,7,8],[6,7,8]]
    elif x == 'F':
        h = 'URDL'
        i = [[6,7,8],[0,3,6],[2,1,0],[8,5,2]]
    elif x == 'B':
        h = 'ULDR'
        i = [[2,1,0],[0,3,6],[6,7,8],[8,5,2]]
    elif x == 'L':
        h = 'UFDB'
        i = [[0,3,6],[0,3,6],[0,3,6],[8,5,2]]
    else:
        h = 'UBDF'
        i = [[8,5,2],[0,3,6],[8,5,2],[8,5,2]]
    if y == '+': j = 3
    else: j = 1
    for k in range(j):
        t1, t2, t3 = c[h[0]][i[0][0]], c[h[0]][i[0][1]], c[h[0]][i[0][2]]
        for l in range(3):
            for ll in range(3):
                c[h[l]][i[l][ll]] = c[h[l+1]][i[l+1][ll]]
        c[h[3]][i[3][0]], c[h[3]][i[3][1]], c[h[3]][i[3][2]] = t1, t2, t3
        c[x][0], c[x][1], c[x][2], c[x][5], c[x][8], c[x][7], c[x][6], c[x][3] = c[x][2], c[x][5], c[x][8], c[x][7], c[x][6], c[x][3], c[x][0], c[x][1]



for _ in range(int(input())):
    c = {d: [e]*9 for d, e in zip('UDFBLR', 'wyrogb')}
    n = int(input())
    m = input().split()
    for o in m:
        rotate(o[0], o[1])

    print(''.join(c['U'][0:3]))
    print(''.join(c['U'][3:6]))
    print(''.join(c['U'][6:9]))