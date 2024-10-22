"""
공백 없는 A+B
"""
N = input()
if len(N) == 2:
    print(int(N[0]) + int(N[1]))
elif len(N) == 3:
    if N[1] == '0':
        print(10 + int(N[2]))
    elif N[2] == '0':
        print(int(N[0]) + 10)
elif len(N) == 4:
    print(20)