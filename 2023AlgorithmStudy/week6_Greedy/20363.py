"""
당근 키우기
X: 온기, Y: 수분
1햇빛: 1온기
10햇빛: -1수분
1물: 1수분
10물: -1온기
"""
X, Y = map(int, input().split())
# if X > Y: print(X + Y + Y//10)
# else: print(X + Y + X//10)
print(X + Y + min(X, Y)//10)