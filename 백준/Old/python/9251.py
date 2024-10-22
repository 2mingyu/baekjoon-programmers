"""
LCS

어렵다 진짜
https://myjamong.tistory.com/317
"""
s1, s2 = input(), input()
l1, l2 = len(s1), len(s2)
c = [0] * l2

for i1 in range(l1):
    tmp = 0
    for i2 in range(l2):
        if tmp < c[i2]:
            tmp = c[i2]
        elif s1[i1] == s2[i2]:
            c[i2] = tmp + 1
print(max(c))