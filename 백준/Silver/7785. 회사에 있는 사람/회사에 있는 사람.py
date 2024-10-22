n = int(input())
s = set()
for _ in range(n):
    x = input().split()
    if x[1] == 'enter':
        s.add(x[0])
    else:
        s.remove(x[0])
for e in sorted(list(s), reverse=True):
    print(e)