"""
미터계
"""
N = list(input())
s = 0
for i in range(len(N)):
    if int(N[-(i+1)]) > 4:
        s += (int(N[-(i+1)])-1) * 9**i
    else:
        s += int(N[-(i+1)]) * 9**i
print(s)