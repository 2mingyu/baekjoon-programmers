N = int(input())
l = list(map(int, input().split()))
M = max(l)
s = 0
for i in l:
    s += i/M*100
print(s/N)