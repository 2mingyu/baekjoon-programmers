"""
성냥개비

INU 코드페스티벌 2021 B
"""
d = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 0: 6}
N = int(input()) - 4
for n1 in d:
    for n2 in d:
        for n3 in d:
            for n4 in d:
                tmp = (n1*10 + n2) + (n3*10 + n4)
                if tmp < 100:
                    n5 = tmp // 10
                    n6 = tmp % 10
                    if d[n1] + d[n2] + d[n3] + d[n4] + d[n5] + d[n6] == N:
                        print(str(n1)+str(n2)+'+'+str(n3)+str(n4)+'='+str(n5)+str(n6))
                        exit(0)
print('impossible')