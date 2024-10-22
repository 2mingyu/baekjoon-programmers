"""
일곱 난쟁이
"""
a = []
for _ in range(9): a.append(int(input()))
for i in range(9):
    b = a[0:i]+a[i+1:9]
    for j in range(8):
        c = b[0:j]+b[j+1:9]
        if sum(c) == 100:
            for k in sorted(c):
                print(k)
            exit(0)