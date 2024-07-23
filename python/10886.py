"""
0 = not cute / 1 = cute
"""
N = int(input())
a = 0
for _ in range(N):
    if int(input()): a += 1
print('Junhee is' + [' not ', ' '][a > N//2] + 'cute!')