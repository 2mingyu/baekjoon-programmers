N = int(input())
l = [input() for _ in range(N)]
s = set(l)
for e in l:
    if e[::-1] in s:
        print(len(e), e[len(e)//2])
        exit()