T = int(input())
for t in range(T):
    N = int(input())
    zero = [1, 0]   # zero[n] : fibonacci(n)에서 0이 나온 횟수
    one = [0, 1]   # one[n] : fibonacci(n)에서 1이 나온 횟수
    for n in range(2, N + 1):
        zero.append(zero[n-1] + zero[n-2])
        one.append(one[n-1] + one[n-2])
    print(zero[N], one[N])