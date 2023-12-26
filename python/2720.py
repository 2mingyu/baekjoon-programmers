"""
세탁소 사장 동혁

25 10 5 1
"""
T = int(input())
for _ in range(T):
    C = int(input())
    Q = C // 25; C %= 25
    D = C // 10; C %= 10
    N = C // 5; C %= 5
    P = C
    print(Q, D, N, P)