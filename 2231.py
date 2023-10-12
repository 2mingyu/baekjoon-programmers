"""
분해합
"""
N=int(input())
for M in range(N):
    if M+sum(list(map(int, str(M))))==N:
        print(M)
        exit(0)
print(0)