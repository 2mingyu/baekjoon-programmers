"""
소인수분해
"""
N=int(input())
i=2
while N>1:
    if N%i:i+=1
    else:
        print(i)
        N/=i