"""
Fill the Rowboats!
"""
l = []
for i in range(1, int(input())+1):
    l.append(str(i))
    if i % 6 == 0: l.append('Go!')
if l[-1] != 'Go!': l.append('Go!')
print(' '.join(l))