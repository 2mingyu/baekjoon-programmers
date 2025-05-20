N = int(input())
A = input()
B = ''
i = 0
while i < N:
    if i+1 < N and A[i:i+2] == 'PS':
        B += 'PS'
        i += 2
        while i < N and (A[i] == '4' or A[i] == '5'):
            i += 1
    else:
        B += A[i]
        i += 1
print(B)