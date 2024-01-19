"""
타임 카드
"""
for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    t1 = h1*60*60 + m1*60 + s1
    t2 = h2*60*60 + m2*60 + s2
    t3 = t2 - t1
    s3 = t3 % 60
    t3 //= 60
    m3 = t3 % 60
    t3 //= 60
    h3 = t3
    print(h3, m3, s3)