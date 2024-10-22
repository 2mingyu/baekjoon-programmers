"""
N-Queen

8x8 (0,0) ~ (7,7) 칸이라고 치면,
(0,0)경우 = (7,7)경우 = (0,7)경우 = (7,0)경우
0,1 = 1,0 = 6,0 = 1,7 = 0,6 = 7,1 = 7,6 = 6,7
대칭대칭 ...
===========
맨 윗줄을 출발지로 하고, 아래로 내려가면서 탐색? DFS.. BFS..
양쪽 대칭이니까 짝수의 경우 range(N/2) 하고 2배
홀수의 경우 range(N/2) 하고 2배 + (N/2+1)

0번째줄에 N번칸에 놓여있으면
1번째줄은 N-1번칸 N+1번칸 불가능
M번째줄은 N-M번칸 N+M번칸 불가능
몇번째줄이던 N번칸 불가능

A번째줄에 N번칸에 놓여있으면
A+1번째줄은 N-1번칸 N+1번칸 불가능
M번째줄은 N-(M-A)번칸 N+(M-A)번칸 불가능
몇번째줄이던 N번칸 불가능

ban_list는 in 연산만 쓰니까 list대신 set 쓰자

Python3로는 안되고 PyPy3로는 됨
"""
def function(x, l, c):
    now_l = l + [x]
    now_line = len(now_l)
    if now_line == N: return 1
    ban_list_set = set()
    for i in range(len(now_l)):
        ban_list_set.add(now_l[i])
        ban_list_set.add(now_l[i]-(now_line-i))
        ban_list_set.add(now_l[i]+(now_line-i))
    for i in range(N):
        if i not in ban_list_set:
            c += function(i, now_l, 0)
    return c

N = int(input())
line_list = []
count = 0
for i in range(N//2):
    count += function(i, line_list, 0) * 2
if N%2:
    count += function(N//2, line_list, 0)
print(count)