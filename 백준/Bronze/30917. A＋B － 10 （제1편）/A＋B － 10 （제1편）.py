A = B = 0
for a in range(1, 10):
    print("? A", a, flush=True)
    resp = int(input())
    if resp == 1:
        A = a
        break
for b in range(1, 10):
    print("? B", b, flush=True)
    resp = int(input())
    if resp == 1:
        B = b
        break
print("!", A+B)