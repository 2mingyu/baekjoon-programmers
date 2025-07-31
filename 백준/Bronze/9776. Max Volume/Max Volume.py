n = int(input())
M = 0
for _ in range(n):
    l = input().split()
    r = float(l[1])
    h = float(l[2]) if len(l)>2 else 1
    pi = 3.14159
    if l[0] == 'C':
        V = (1/3)*pi*r**2*h
    elif l[0] == 'L':
        V = pi*r**2*h
    elif l[0] == 'S':
        V = (4/3)*pi*r**3
    M = max(M, V)
print(f'{M:.3f}')