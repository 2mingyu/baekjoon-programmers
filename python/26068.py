"""
치킨댄스를 추는 곰곰이를 본 임스
"""
N = int(input())
r = 0
for _ in range(N):
    x = int(input()[2:])
    if x <= 90: r += 1
print(r)