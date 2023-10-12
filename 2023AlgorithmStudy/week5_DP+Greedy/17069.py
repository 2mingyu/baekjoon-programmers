"""
방법(N,N)=방법(N-1,N)+방법(N-1,N-1)+방법(N,N-1)
ex)
m(3,3)=m(2,3)+m(2,2)+m(3,2)
      =1+0+0
시작 위치는 (1,2)
(a,b)에서 (a+1,b) (a+1,b+1) (a,b+1) 갈 수 있음
벽(1)을 만나면 m(벽) = 0
=====여기 위 까지는 회전모양 고려가 안 됨..
=====가로->세로, 세로->가로 의 경우도 포함되어있음
=====대각선으로 벽 긁는 것도 고려가 안 됨..
방법(행,열,가로) = 방법(행,열-1,가로)+방법(행-1,열,대각)
방법(행,열,세로) = 방법(행-1,열,세로)+방법(행-1,열,대각)
방법(행,열,대각) = 방법(행-1,열-1,가로)+방법(행-1,열-1,대각)+방법(행-1,열-1,세로)
c : 0=가로, 1=대각, 2=세로
(a,b,0)에서 (a,b+1,0) (a+1,b+1,1)           갈 수 있음
(a,b,1)에서 (a,b+1,0) (a+1,b+1,1) (a+1,b,2) 갈 수 있음
(a,b,2)에서           (a+1,b+1,1) (a+1,b,2) 갈 수 있음
벽 위치 고려하고
"""
N = int(input())
house = [[1] * (N+2)]
m = [[[0 for k in range(3)] for j in range(N+2)] for i in range(N+2)]
for _ in range(N):
    tmp = [1] + list(map(int, input().split())) + [1]
    house.append(tmp)
house.append([1] * (N+2))
m[1][2][0] = 1
for row in range(1, N+1):
    for col in range(2, N+1):
        if house[row][col+1] != 1:
            m[row][col+1][0] += m[row][col][0]  # 가로->가로
            m[row][col+1][0] += m[row][col][1]  # 대각->가로
        if house[row][col+1] != 1 and house[row+1][col+1] !=1  and house[row+1][col] != 1:
            m[row+1][col+1][1] += m[row][col][0]    # 가로->대각
            m[row+1][col+1][1] += m[row][col][1]    # 대각->대각
            m[row+1][col+1][1] += m[row][col][2]    # 세로->대각
        if house[row+1][col] != 1:
            m[row+1][col][2] += m[row][col][1]    # 대각->세로
            m[row+1][col][2] += m[row][col][2]    # 세로->세로
print(sum(m[N][N]))