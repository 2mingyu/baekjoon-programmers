for _ in range(3):
    t1, t2 = input().split()
    h1, m1, s1 = map(int, t1.split(':'))
    h2, m2, s2 = map(int, t2.split(':'))
    r = 0
    while True:
        if int(str(h1)+str(m1)+str(s1)) % 3 == 0:
            r += 1
        if h1 == h2 and m1 == m2 and s1 == s2:
            break
        s1 += 1
        if s1 == 60:
            s1 = 0
            m1 += 1
            if m1 == 60:
                m1 = 0
                h1 += 1
                if h1 == 24:
                    h1 = 0
    print(r)