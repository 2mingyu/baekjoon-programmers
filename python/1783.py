"""
병든 나이트

처음에 dfs인 줄 알았는데, 그냥 규칙 찾기
"""
N, M = map(int,input().split())
if N == 1:
    print(1)
elif N == 2:
    if M < 3:
        print(1)
    elif M < 5:
        print(2)
    elif M < 7:
        print(3)
    else:
        print(4)
else:
    if M == 1:
        print(1)
    elif M == 2:
        print(2)
    elif M == 3:
        print(3)
    elif M == 4:
        print(4)
    elif M == 5:
        print(4)
    elif M == 6:
        print(4)
    elif M == 7:
        print(5)
    else:
        print(M-2)