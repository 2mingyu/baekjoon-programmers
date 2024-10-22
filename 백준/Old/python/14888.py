"""
연산자 끼워넣기
"""
def f(value, c):
    global maxvalue, minvalue
    s = sum(c)
    if s == 0:
        maxvalue = max(maxvalue, value)
        minvalue = min(minvalue, value)
        return
    if c[0] > 0: f(value+A[N-s], [c[0]-1, c[1], c[2], c[3]])
    if c[1] > 0: f(value-A[N-s], [c[0], c[1]-1, c[2], c[3]])
    if c[2] > 0: f(value*A[N-s], [c[0], c[1], c[2]-1, c[3]])
    if c[3] > 0:
        if value < 0: f(-(abs(value)//A[N-s]), [c[0], c[1], c[2], c[3]-1])
        else: f(value//A[N-s], [c[0], c[1], c[2], c[3]-1])

N = int(input())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
maxvalue = -(10**9)
minvalue = 10**9
f(A[0], C)
print(maxvalue)
print(minvalue)