"""
콰트로치즈피자
"""
n = int(input())
l = []
for t in input().split():
    if t[-6:] == 'Cheese' and t not in l:
        l.append(t)
print('yummy' if len(l) >= 4 else 'sad')