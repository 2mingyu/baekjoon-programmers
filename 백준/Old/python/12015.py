"""
가장 긴 증가하는 부분 수열 2

LIS
"""
def f(n):
    s = 0
    e = len(l) - 1
    while s <= e:
        m = (s+e) //2
        if l[m] == n:
            return m
        elif l[m] < n:
            s = m+1
        else:
            e = m-1
    return s

N = int(input())
A = list(map(int, input().split()))
l = [A[0]]

for i in range(N):
    if A[i] > l[-1]:
        l.append(A[i])
    else:
        j = f(A[i])
        l[j] = A[i]

print(len(l))
