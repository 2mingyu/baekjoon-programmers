"""
Judging Moose
"""
ℓ, r = map(int, input().split())
if ℓ == r == 0: print('Not a moose')
elif ℓ == r: print('Even', ℓ*2)
else: print('Odd', max(ℓ, r)*2)