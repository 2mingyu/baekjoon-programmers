"""
탁구 경기
"""
N = int(input())
X = Y = 0
for _ in range(N):
    if input() == 'D': X += 1
    else: Y += 1
    if abs(X-Y) >= 2: break
print(str(X)+':'+str(Y))