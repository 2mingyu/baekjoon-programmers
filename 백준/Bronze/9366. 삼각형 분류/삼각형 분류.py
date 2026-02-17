T = int(input())
for x in range(1, T + 1):
    A, B, C = sorted(map(int, input().split()))
    if A + B <= C:
        r = "invalid!"
    elif A == B == C:
        r = "equilateral"
    elif A == B or B == C or A == C:
        r = "isosceles"
    else:
        r = "scalene"
    print(f"Case #{x}: {r}")