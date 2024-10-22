"""
여중생 파댕이와 공부를
"""
N, M = map(int, input().split())
for _ in range(N):
    input()
    s = input()
    input()
    p = []
    a = b = c = -1
    for i in range(8*M):
        if s[i] == '+':
            p.append([int(s[i-1]), int(s[i+1]), int(float(s[i+3:i+5]))])
    o1 = ''
    o2 = ''
    o3 = ''
    for q in p:
        if q[0] + q[1] == q[2]:
            t = str(q[0]) + '+' + str(q[1]) + '=' + str(q[2])
            if len(str(q[2])) == 1:
                o1 += '.*****..'
                o2 += '*' + t + '*.'
                o3 += '.*****..'
            else:
                o1 += '.******.'
                o2 += '*' + t + '*'
                o3 += '.******.'
        else:
            t = str(q[0]) + '/' + str(q[1]) + '=' + str(q[2])
            o1 += '.../....'
            o3 += './......'
            if len(str(q[2])) == 1:
                o2 += '.' + t + '..'
            else:
                o2 += '.' + t + '.'
    print(o1)
    print(o2)
    print(o3)