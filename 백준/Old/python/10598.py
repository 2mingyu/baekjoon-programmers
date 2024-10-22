"""
Knockout Racing
"""
n, m = map(int, input().split())
cars = []
for i in range(n):
    a, b = map(int, input().split())
    cars.append((a, b))
for j in range(m):
    x, y, t = map(int, input().split())
    count = 0
    for a, b in cars:
        period = 2*abs(b-a)
        time_in_period = t % period
        if time_in_period <= abs(b - a):
            current_position = a + (b - a) // abs(b - a) * time_in_period
        else:
            current_position = b + (a - b) // abs(b - a) * (time_in_period - abs(b - a))
        if x <= current_position <= y:
            count += 1

    print(count)