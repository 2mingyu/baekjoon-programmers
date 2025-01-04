N = input()
F = int(input())

for i in range(10):
    for j in range(10):
        t = int(N[:-2] + str(i) + str(j))
        if t % F == 0:
            print(str(i) + str(j))
            exit()