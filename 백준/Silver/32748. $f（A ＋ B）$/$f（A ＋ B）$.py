d = list(map(int, input().split()))


def f(X):
    if len(X) == 1:
        return str(d[int(X)])
    return ''.join([f(x) for x in X])


def r(Y):
    if len(Y) == 1:
        return str(d.index(int(Y)))
    return ''.join([r(y) for y in Y])


fA, fB = input().split()
A, B = r(fA), r(fB)
print(f(str(int(A)+int(B))))