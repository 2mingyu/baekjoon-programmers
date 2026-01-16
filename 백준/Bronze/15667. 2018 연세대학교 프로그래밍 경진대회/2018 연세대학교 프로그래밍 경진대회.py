N = int(input())
for K in range(101):
    if 1 + K + K**2 == N:
        print(K)
        break