S = int(input())
D = float(input())
T = float(input())
print(['MADE IT', 'FAILED TEST'][5280/3600*S*T <= D])