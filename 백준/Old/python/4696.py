"""
St. Ives
"""
while True:
    i = float(input())
    if not i: break
    print("{:.2f}".format(round(1 + i + i**2 + i**3 + i**4, 2)))