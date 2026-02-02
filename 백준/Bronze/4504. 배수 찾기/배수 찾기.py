n = int(input())
while True:
    k = int(input())
    if k == 0: break
    x = ["", " NOT"][bool(k%n)]
    print(f"{k} is{x} a multiple of {n}.")