"""
Triples
"""
def T(m, j):
    s = set()
    for z in range(m+1):
        for y in range(z+1):
            for x in range(y+1):
                if x**j + y**j == z**j:
                    s.add((x, y, z))
    return s

def card(s):
    return len(s)

def S(m, n):
    return(sum([card(T(m, j)) for j in range(2, n+1)]))

m = int(input())
n = int(input())
print(S(m, n))