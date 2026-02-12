import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t + 1):
    p = int(input())
    m = {}
    for _ in range(p):
        a, b = input().split()
        m[a] = b
        m[b] = a

    q = int(input())

    print(f"Test case #{tc}:")
    for _ in range(q):
        s = input().strip()

        l, r = 0, len(s) - 1
        ok = 1
        while l < r:
            a, b = s[l], s[r]
            if a == b:
                pass
            elif m.get(a) == b:
                pass
            else:
                ok = 0
                break
            l += 1
            r -= 1

        print(s, "YES" if ok else "NO")
    print()
