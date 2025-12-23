n = int(input())
for i in range(1, n+1):
    print(f"Scenario #{i}:")
    a, b, c = sorted(map(int, input().split()))
    print(['no', 'yes'][a**2 + b**2 == c**2])
    print()