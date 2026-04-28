import sys
input = sys.stdin.readline

P, K = input().split()
P = int(P)
K = int(K)

sieve = [True] * K
if K > 2:
    sieve[0] = sieve[1] = False
    for i in range(2, int(K**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, K, i):
                sieve[j] = False
primes = [i for i in range(2, K) if sieve[i]]

r = -1
for p in primes:
    if P % p == 0:
        r = p
        break

if r == -1:
    print("GOOD")
else:
    print(f"BAD {r}")