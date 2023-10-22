"""
배수와 약수
"""
while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    if a<=b and b%a == 0: print('factor')
    elif b<=a and a%b ==0: print('multiple')
    else: print('neither')