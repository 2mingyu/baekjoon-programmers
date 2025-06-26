N = int(input())
S = input()
O = S.count('O')
print('Yes' if O >= N-O else 'No')