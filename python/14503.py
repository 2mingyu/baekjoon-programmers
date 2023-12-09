"""
로봇 청소기
"""
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

result = 0
while True:
    move = False
    if room[r][c] == 0:
        room[r][c] = 2
        result += 1
    else:
        for _ in range(4):
            d = (d+3) % 4
            if d == 0:
                if r-1 >= 0 and room[r-1][c] == 0:
                    r = r-1
                    move = True
                    break
            elif d == 1:
                if c+1 < M and room[r][c+1] == 0:
                    c = c+1
                    move = True
                    break
            elif d == 2:
                if r+1 < N and room[r+1][c] == 0:
                    r = r+1
                    move = True
                    break
            elif d == 3:
                if c-1 >= 0 and room[r][c-1] == 0:
                    c = c-1
                    move = True
                    break
        if move: continue
        else:
            if d == 0:
                if r+1 < N and room[r+1][c] != 1:
                    r = r+1
                    continue
            elif d == 1:
                if c-1 >= 0 and room[r][c-1] != 1:
                    c = c-1
                    continue
            elif d == 2:
                if r-1 >= 0 and room[r-1][c] != 1:
                    r = r-1
                    continue
            elif d == 3:
                if c+1 < M and room[r][c+1] != 1:
                    c = c+1
                    continue
            break

print(result)