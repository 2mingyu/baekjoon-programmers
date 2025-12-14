import sys
a = sys.stdin.readlines()
n = []
for i in a:
    for j in i.split():
        n.append(int(j[::-1]))
for i in sorted(n[1:]):
    print(i)