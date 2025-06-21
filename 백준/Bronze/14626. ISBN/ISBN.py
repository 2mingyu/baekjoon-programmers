S = input()
a = 0
w = 1
for i in range(13):
    if S[i] != '*':
        if i%2: a += 3*int(S[i])
        else: a += int(S[i])
    else:
        if i%2: w = 3
for x in range(10):
    if (a+w*x) % 10 == 0:
        print(x)
        break