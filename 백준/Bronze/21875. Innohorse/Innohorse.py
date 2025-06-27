A = input()
B = input()
l = [abs(ord(A[0])-ord(B[0])), abs(int(A[1])-int(B[1]))]
print(min(l), max(l))