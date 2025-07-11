n = int(input())
ta = tb = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a < ta or b < tb:
        print("no")
        exit()
    ta, tb = a, b
print("yes")