S = input()
A = B = 0
C = ''
r = ''
for i in range(len(S)):
    if S[i].isdigit() and S[i+1] in '+-*/':
        A, B, C = int(S[:i+1], 8), int(S[i+2:], 8), S[i+1]
        break
if C == '+':
    r = oct(A + B)
elif C == '-':
    r = oct(A - B)
elif C == '*':
    r = oct(A * B)
elif C == '/':
    if B == 0:
        r = 'invalid'
    else:
        r = oct(A//B)
print(r.replace('0o', ''))
