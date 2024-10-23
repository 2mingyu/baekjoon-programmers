def solution(array):
    n = [0] * 1000
    for e in array:
        n[e] += 1
    t = []
    m = -1
    for i in range(1000):
        if n[i] > m:
            t = [i]
            m = n[i]
        elif n[i] == m:
            t.append(i)
    if len(t) == 1:
        return t[0]
    return -1