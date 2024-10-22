"""
체스판 다시 칠하기
i, j는 자르기
k, l은 자른 판 안에서 위치
"""
N, M = map(int, input().split())
board = []
for _ in range(N): board.append(input())
case1 = 'WBWBWBWB'
case2 = 'BWBWBWBW'
result = M * N
for i in range(N-7):
    for j in range(M-7):
        count1 = count2 = 0
        for k in range(8):
            for l in range(8):
                if k%2:
                    if case1[l] != board[i+k][j+l]: count1 += 1
                    if case2[l] != board[i+k][j+l]: count2 += 1
                else:
                    if case2[l] != board[i+k][j+l]: count1 += 1
                    if case1[l] != board[i+k][j+l]: count2 += 1
        result = min(result, count1, count2)
print(result)