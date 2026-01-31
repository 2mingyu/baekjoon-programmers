T = int(input())
for _ in range(T):
    a = input()
    b = input()
    s = 0
    for i in range(len(a)):
        s += a[i] != b[i]
    print(f"Hamming distance is {s}.")