"""
3차원 지뢰찾기
"""
R, C, H = map(int, input().split())
cube = [[list(input()) for _ in range(R)] for _ in range(H)]
counts = [[[0]*C for _ in range(R)] for _ in range(H)]

for h in range(H):
    for r in range(R):
        for c in range(C):
            if cube[h][r][c] == '*':
                for i in (-1, 0, 1):
                    x = h + i
                    if 0 <= x < H:
                        for j in (-1, 0, 1):
                            y = r + j
                            if 0 <= y < R:
                                for k in (-1, 0, 1):
                                    z = c + k
                                    if 0 <= z < C:
                                        if cube[x][y][z] != '*':
                                            counts[x][y][z] += 1

for h in range(H):
    for r in range(R):
        for c in range(C):
            if cube[h][r][c] == '*':
                pass
            else:
                cube[h][r][c] = str(counts[h][r][c] % 10)

for h in range(H):
    for r in range(R):
        print(''.join(cube[h][r]))
