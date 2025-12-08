i = 1
while True:
    n0 = int(input())
    if n0 == 0: break
    n1 = 3*n0
    print(f"{i}. {['even', 'odd'][n1%2]} {n0//2}")
    i += 1