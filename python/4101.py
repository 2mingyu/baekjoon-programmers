"""
크냐?
"""
while True:
    i = input()
    if i == '0 0': break
    i = i.split()
    if int(i[0]) > int(i[1]): print('Yes')
    else: print('No')