"""
Sounds fishy!
"""
l = [int(input()) for _ in range(4)]
a = 0
b = 0
for i in range(3):
    if l[i+1] > l[i]:
        a += 1
    elif l[i+1] < l[i]:
        a -= 1
    else:
        b += 1

if b == 3: print('Fish At Constant Depth')
elif a == 3: print('Fish Rising')
elif a == -3: print('Fish Diving')
else: print('No Fish')