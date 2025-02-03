N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
C = []
i = 100
while i > 0:
    if i in A and i in B:
        C.append(i)
        A = A[A.index(i)+1:]
        B = B[B.index(i)+1:]
        i = 100
    else:
        i -= 1
print(len(C))
print(*C)