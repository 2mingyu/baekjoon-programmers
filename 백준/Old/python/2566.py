"""
최댓값
"""
m, y, x = 0, 0, 0
for i in range(9):
    n = input().split()
    for j in range(9):
        if int(n[j]) > m:
            m, y, x = int(n[j]), i, j
print(m)
print(y+1, x+1)