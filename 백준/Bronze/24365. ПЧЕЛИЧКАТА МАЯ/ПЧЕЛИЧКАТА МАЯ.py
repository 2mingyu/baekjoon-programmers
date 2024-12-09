A, B, C = map(int, input().split())
N = (A + B + C) // 3
R = N - A 
B -= R
R += N - B
print(R)