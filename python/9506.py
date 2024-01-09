"""
약수들의 합
"""
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1: break
    l = []
    s = 0
    for i in range(1, n):
        if n % i == 0:
            l.append(str(i))
            s += i
    if n == s:
        print(n, end=" = ")
        print(' + '.join(l))
    else:
        print(n, end = " ")
        print("is NOT perfect.")