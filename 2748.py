"""
피보나치 수 2
"""
F=[0,1]
for i in range(2,91):F.append(F[i-1]+F[i-2])
print(F[int(input())])