N = int(input())
l = input().split()
d = {}
for i in range(N):
    if l[i] in d:
        d[l[i]] += 1
        if d[l[i]] > 4:
            print(i+1)
            exit()
    else:
        d[l[i]] = 1
print(0)