A, B, C = map(int, input().split(':'))
l = [[A, B, C],
     [A, C, B],
     [B, A, C],
     [B, C, A],
     [C, A, B],
     [C, B, A]]
r = 0
for e in l:
    if 1 <= e[0] <= 12 and 0 <= e[1] <= 59 and 0 <= e[2] <= 59:
        r += 1
print(r)