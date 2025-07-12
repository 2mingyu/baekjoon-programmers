a, b, c = input().split()
for d in '+-*/':
    e = a+d+b
    if eval(e) == int(c):
        print(e+'='+c)
        exit()
    e = b+d+c
    if int(a) == eval(e):
        print(a+'='+e)
        exit()