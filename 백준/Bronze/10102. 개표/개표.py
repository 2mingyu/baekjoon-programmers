V = int(input())
A = input().count('A')
B = V-A
if A > B: print('A')
elif B > A: print('B')
else: print('Tie')