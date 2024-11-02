T = int(input())
for x in range(T):
    N, B = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    y = 0
    while A:
        b = A.pop()
        if B-b < 0:
            break
        B -= b
        y += 1
    print(f"Case #{x+1}: {y}")