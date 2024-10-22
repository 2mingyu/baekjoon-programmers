"""
ROT13
"""
v = 'aiyeou'
c = 'bkxznhdcwgpvjqtsrlmf'

def f(x):
    y = True
    if x.isupper():
        y = False
        x = x.lower()
    if x in v:
        x = v[(v.index(x)+3)%6]
    elif x in c:
        x = c[(c.index(x)+10)%20]
    else: return x
    if y: return x
    else: return x.upper()

while True:
    try:
        s = input()
        r = ''
        for a in s:
            r += f(a)
        print(r)
    except:
        break