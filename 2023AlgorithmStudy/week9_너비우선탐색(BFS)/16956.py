"""
늑대와 양
"""
def check():
    for r in range(R):
        for c in range(C):
            if pasture[r][c] == 'S':
                if c-1 >= 0:
                    if pasture[r][c-1] == 'W': return 0
                    elif pasture[r][c-1] == '.': pasture[r][c-1] = 'D'
                if r-1 >= 0:
                    if pasture[r-1][c] == 'W': return 0
                    elif pasture[r-1][c] == '.': pasture[r-1][c] = 'D'
                if c+1 < C:
                    if pasture[r][c+1] == 'W': return 0
                    elif pasture[r][c+1] == '.': pasture[r][c+1] = 'D'
                if r+1 < R:
                    if pasture[r+1][c] == 'W': return 0
                    elif pasture[r+1][c] == '.': pasture[r+1][c] = 'D'
    return 1

R, C = map(int, input().split())
pasture = []
for r in range(R): pasture.append(list(input()))
result = check()
print(result)
if result:
    for r in range(R):
        for c in range(C):
            print(pasture[r][c], end="")
        print()