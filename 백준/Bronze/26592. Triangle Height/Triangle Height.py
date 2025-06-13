n = int(input())
for _ in range(n):
    a, b = map(float, input().split())
    h = a*2/b
    print(f"The height of the triangle is {h:.2f} units")