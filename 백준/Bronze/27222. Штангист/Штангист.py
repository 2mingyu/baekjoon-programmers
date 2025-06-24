n = int(input())
l = list(map(int, input().split()))
s = 0
for i in range(n):
    x, y = map(int, input().split())
    if l[i] and y > x: s += y-x
print(s)