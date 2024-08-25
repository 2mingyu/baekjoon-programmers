"""
Centauri Prime (Small2)
"""
T = int(input())
for x in range(T):
    C = input()
    if C[-1] in 'yY': Y = 'nobody'
    elif C[-1] in 'aeiouAEIOU': Y = 'a queen'
    else: Y = 'a king'
    print(f'Case #{x+1}: {C} is ruled by {Y}.')