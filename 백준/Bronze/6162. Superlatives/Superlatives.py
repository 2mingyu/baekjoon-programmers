K = int(input())
for x in range(1, K + 1):
    print(f"Data Set {x}:")
    E, A = map(int, input().split())

    if E <= A:
        print("no drought")
    else:
        if E <= 5 * A:
            print("drought")
        else:
            m = 0
            f = 5
            while E > f * A:
                m += 1
                f *= 5 

            print("mega " * m + "drought")
    print()
