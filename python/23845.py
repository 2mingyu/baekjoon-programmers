"""
마트료시카

INU 코드페스티벌 2021 E

마트료시카를 최대한 길게?
"""
N = int(input())
X = sorted(list(map(int, input().split())))
Y = [0] * (2*10**5)
for x in X:
    Y[x] += 1
r = 0

for i in range(N):
    if Y[X[i]] >= 1:
        Y[X[i]] -= 1
        Q = X[i]
        T = 1
        j = X[i] + 1
        while True:
            if Y[j] >= 1:
                Q = j
                Y[j] -= 1
                T += 1
                j += 1
            else:
                r += Q * T
                break
print(r)