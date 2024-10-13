"""
피보나치 비스무리한 수열
"""
f = [1, 1, 1]
for i in range(116):
    f.append(f[-1] + f[-3])
print(f[int(input())-1])