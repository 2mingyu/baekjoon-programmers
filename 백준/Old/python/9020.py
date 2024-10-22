"""
골드바흐의 추측
"""
isPrime = [1] * 10000
for i in range(2, 10000):
    if isPrime[i]:
        ii = i+i
        while ii < 10000:
            isPrime[ii] = 0
            ii += i

for _ in range(int(input())):
    n = int(input())
    a = b = n//2
    while not isPrime[a] or not isPrime[b]:
        if a%2:
            a -= 2
            b += 2
        else:
            a -= 1
            b += 1
    print(a, b)