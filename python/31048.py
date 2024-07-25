"""
Last Factorial Digit
"""
T = int(input())
for _ in range(T):
    N = int(input())
    a = 1
    for i in range(1, N+1):
        a *= i
    print(str(a)[-1])