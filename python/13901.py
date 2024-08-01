"""
로봇
"""
R, C = map(int, input().split())
room = [[0]*(C+2) for _ in range(R+2)]
for i in range(R+2):
    room[i][0] = 1
    room[i][C+1] = 1
for j in range(C+2):
    room[0][j] = 1
    room[R+1][j] = 1
k = int(input())
for _ in range(k):
    br, bc = map(int, input().split())
    room[br+1][bc+1] = 1
sr, sc = map(int, input().split())
sr, sc = sr+1, sc+1
room[sr][sc] = 1
command = input().split()
i = 0
while True:
    if room[sr-1][sc] == room[sr+1][sc] == room[sr][sc-1] == room[sr][sc+1] == 1:
        break
    nr = nc = 0
    if command[i] == '1':
        nr, nc = sr-1, sc
    elif command[i] == '2':
        nr, nc = sr+1, sc
    elif command[i] == '3':
        nr, nc = sr, sc-1
    elif command[i] == '4':
        nr, nc = sr, sc+1
    if not room[nr][nc]:
        room[nr][nc] = 1
        sr, sc = nr, nc
    else:
        i = (i + 1) % 4
print(sr-1, sc-1)