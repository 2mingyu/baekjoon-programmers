T = int(input())
for _ in range(T):
    I = input().split()
    N, P = int(I[0]), list(I[1])
    if N == 1:
        if P[0] == '4':
            print(6, 3)
        else:
            print(4, 2)
    else:
        s = sum(map(int, P))
        i = 0
        j = 0
        k = 1
        while i < N:
            if int(P[j]) != k and (s - int(P[j]) + k) % 3 == 0:
                Q = ''.join(P[:j]) + str(k) + ''.join(P[j+1:])
                print(Q, 3)
                i += 1
            k = (k+1)%10
            if k == 0:
                j += 1