A, B, C = map(int, input().split())
X1, X2, Y1, Y2 = map(int, input().split())
r = "Lucky"

if B and Y1 < -(A*X1 + C) / B < Y2:
    r = "Poor"
elif B and Y1 < -(A*X2 + C) / B < Y2:
    r = "Poor"
elif A and X1 < -(B*Y1 + C) / A < X2:
    r = "Poor"
elif A and X1 < -(B*Y2 + C) / A < X2:
    r = "Poor"

print(r)