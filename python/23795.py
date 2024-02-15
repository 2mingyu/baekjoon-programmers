"""
사장님 도박은 재미로 하셔야 합니다
"""
s = 0
while True:
    i = int(input())
    if i < 0: break
    s += i
print(s)