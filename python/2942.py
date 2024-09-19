"""
퍼거슨과 사과
"""
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def f(a):
    d = []
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            d.append(i)
            if i != a // i:
                d.append(a // i)
    return sorted(d)


R, G = map(int, input().split())
N = gcd(R, G)
D = f(N)
for X in D:
    print(X, R//X, G//X)