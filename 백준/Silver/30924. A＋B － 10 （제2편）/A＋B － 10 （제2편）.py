import random

c = list(range(1, 10001))
random.shuffle(c)

for a in c:
    print("? A", a, flush=True)
    resp = int(input())
    if resp == 1:
        A = a
        break
for b in c:
    print("? B", b, flush=True)
    resp = int(input())
    if resp == 1:
        B = b
        break
print("!", A+B)