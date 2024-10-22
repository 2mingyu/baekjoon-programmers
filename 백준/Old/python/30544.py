"""
Cuckoo! Cuckoo!
"""
H, M = map(int, input().split(':'))
N = int(input())
if M == 0: N -= H
elif M in [15, 30, 45]: N -= 1
while N > 0:
    if 0 <= M < 15: M = 15
    elif 15 <= M < 30: M = 30
    elif 30 <= M < 45: M = 45
    else: M = 0
    if M == 0:
        H += 1
        if H > 12:
            H -= 12
        N -= H
    else:
        N -= 1
print(f"{H:02d}:{M:02d}")