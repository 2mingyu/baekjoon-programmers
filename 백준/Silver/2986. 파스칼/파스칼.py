N = int(input())
c = 0
d = 1
for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
        d = N//i
        break
print(N-d)