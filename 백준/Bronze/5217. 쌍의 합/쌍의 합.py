T = int(input())

for _ in range(T):
    n = int(input())
    print(f"Pairs for {n}:", end="")

    first = True
    for a in range(1, n):
        b = n - a
        if a >= b:
            break
        if first:
            print(f" {a} {b}", end="")
            first = False
        else:
            print(f", {a} {b}", end="")

    print()