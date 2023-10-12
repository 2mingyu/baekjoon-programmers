def fibonacci(n):
    if n == 0:
        results[0] += 1
        return 0
    elif n == 1:
        results[1] += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

T = int(input())
for t in range(T):
    results = [0, 0]
    fibonacci(t)
    print(t, results[0], results[1])