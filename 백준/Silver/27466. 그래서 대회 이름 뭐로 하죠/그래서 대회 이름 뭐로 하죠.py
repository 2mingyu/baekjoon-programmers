N, M = map(int, input().split())
S = input()
O = A1 = A2 = -1
for i in range(N-1, -1, -1):
    if O == -1 and S[i] not in 'AEIOU':
        O = i
    elif A1 == -1 and S[i] == 'A':
        A1 = i
    elif A2 == -1 and S[i] == 'A':
        A2 = i
if O != -1 and A1 != -1 and A2 != -1 and A2+2 >= M:
    print('YES')
    print(S[M-A2-1:A2]+'AA'+S[O])
else:
    print('NO')