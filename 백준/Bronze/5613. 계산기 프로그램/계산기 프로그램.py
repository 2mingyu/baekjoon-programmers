r = int(input())
while True:
    a = input()
    if a == '=': break
    b = int(input())
    if a == '+': r += b
    elif a == '-': r -= b
    elif a == '*': r *= b
    elif a == '/': r //= b
print(r)