N = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        if N in (i, j, i*j):
            print(1)
            exit()
print(0)