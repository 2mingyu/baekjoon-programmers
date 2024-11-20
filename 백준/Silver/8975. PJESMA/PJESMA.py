N = int(input())
T = set([input() for _ in range(N)])
c = 0
M = int(input())
for i in range(M):
    t = input()
    if t in T:
        c += 1
        T.remove(t)
    if c >= N//2 + bool(N%2):
        print(i+1)
        break