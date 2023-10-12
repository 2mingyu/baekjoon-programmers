"""
패션왕 신해빈
"""
for _ in range(int(input())):
    d = dict()
    for _ in range(int(input())):
        i = input().split()[1]
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    result = 1
    for j in d:
        result *= d[j]+1
    print(result - 1)