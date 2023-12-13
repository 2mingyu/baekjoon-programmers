"""
막대기
"""
X = int(input())
l = [64]
if X == 64:
    print(1)
    exit(0)
while True:
    c = l.pop() // 2
    l.append(c)
    s = sum(l)
    if s == X:
        print(len(l))
        break
    if s < X:
        l.append(c)