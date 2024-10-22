"""
Goodbye, Code Jam
"""
T = int(input())
for x in range(1, T+1):
    z = int(input())
    if z > 4500: y = 'Round 1'
    elif z > 1000: y = 'Round 2'
    elif z > 25: y = 'Round 3'
    else: y = 'World Finals'
    print('Case #' + str(x) + ': ' + y)