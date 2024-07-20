"""
Polynesiaglot (Small1)
"""
for x in range(int(input())):
 c,v=0,1
 for _ in range(int(input().split()[2])):c,v=v,c+v
 print(f'Case #{x+1}: {v}')