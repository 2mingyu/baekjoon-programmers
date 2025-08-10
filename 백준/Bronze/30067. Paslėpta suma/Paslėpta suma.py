l = [int(input()) for _ in range(10)]
s = sum(l)
for i in range(10):
    if s == l[i]*2:
        print(l[i])
        exit()