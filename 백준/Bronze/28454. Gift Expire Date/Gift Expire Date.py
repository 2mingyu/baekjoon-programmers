Y, M, D = map(int, input().split('-'))
r = 0
for _ in range(int(input())):
    A, B, C = map(int, input().split('-'))
    if Y < A:
        r += 1
        continue
    elif Y > A:
        continue
    if M < B:
        r += 1
        continue
    elif M > B:
        continue
    if D <= C:
        r +=1
print(r)