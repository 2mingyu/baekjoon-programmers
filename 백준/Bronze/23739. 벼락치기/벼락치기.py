N = int(input())
A = 30
r = 0
for _ in range(N):
    T = int(input())
    if A >= T/2: r += 1
    A -= T
    if A <= 0: A = 30
print(r)