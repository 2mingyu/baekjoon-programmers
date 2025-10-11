T = int(input())
for _ in range(T):
    s = 0
    S = set(input())
    for i in range(65, 91):
        if chr(i) not in S: s += i
    print(s)