"""
작은 수 내기
"""
N = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())))
c = 0
for e in a:
    if e < b[-1]:
        c += 1
        b.pop()
    if c >= (N+1)//2:
        print("YES")
        exit()
print("NO")