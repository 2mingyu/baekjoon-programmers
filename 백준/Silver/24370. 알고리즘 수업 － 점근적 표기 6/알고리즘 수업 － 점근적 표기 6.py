a2,a1,a0 = map(int,input().split())
c1,c2 = map(int,input().split())
n0 = int(input())

def g(x): return c1*(x**2)
def f(x): return a2*x**2 + a1*x + a0
def h(x): return c2*(x**2)

D1 = a1**2 - 4*(a2-c1)*a0
D2 = a1**2 - 4*(a2-c2)*a0

co1 = 0
if a2 == c1:
    if a1 == a0 == 0:
        co1 = True
    else:
        if a1 >= 0: co1 = True
        elif a1 == 0:
            if a0 >= 0: co1 = True
            else: co1 = False
        else: co1 = False
elif a2 < c1: co1 = False
elif D1 < 0:
    if f(n0) >= g(n0): co1 = True
    else: co1 = False
elif D1 == 0:
    if f(n0) >= g(n0): co1 = True
    else: co1 = False
else:
    x1 = (a1 + D1**(1/2)) / (2*(c1 - a2))
    x2 = (a1 - D1**(1/2)) / (2*(c1 - a2))
    x = max(x1, x2)
    if a2 > 0:
        vertex = a1 / (2 * (c1 - a2))
        if f(vertex) > g(vertex):
            co1 = False
        else:
            if x <= n0: co1 = True
            else: co1 = False
    else:
        if n0 <= x: co1 = False
        else: co1 = True

co2 = False
if a2 == c2:
    if a1 == a0 == 0: co2 = True
    else:
        if a1 > 0: co2 = False
        elif a1 == 0:
            if a0 > 0: co2 = False
            else: co2 = True
        else: co2 = True
elif a2 > c2: co2 = False
elif D2 < 0 :
    if f(n0) <= h(n0): co2 = True
    else: co2 = False
elif D2 == 0:
    if f(n0) <= h(n0): co2 = True
    else: co2 = False
else:
    x = (a1 + D2**(1/2)) / (2 * (c2 - a2))
    if a2 > 0:
        vertex = a1 / (2 * (c2 - a2))
        if f(vertex) < h(vertex): co2 = False
        else:
            if x <= n0: co2 = True
            else: co2 = False
    else:
        if x <= n0: co2 = True
        else: co2 = False

print(int(co1 and co2)) 