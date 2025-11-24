S = int(input())
for _ in range(S):
    s = input()
    a = b = 0
    for c in s:
        if c in 'AEIOUaeiou': a += 1
        elif c != ' ': b += 1
    print(b, a)