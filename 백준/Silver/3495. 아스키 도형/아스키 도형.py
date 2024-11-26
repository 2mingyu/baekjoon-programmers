h, w = map(int, input().split())
r = 0
for _ in range(h):
    l = input()
    n = False
    for c in l:
        if c == '.':
            if n:
                r += 1
        else:
            n = not n
            r += 0.5
print(int(r))