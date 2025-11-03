R, C, ZR, ZC = map(int, input().split())
for _ in range(R):
    print((''.join([e*ZC for e in input()])+'\n')*ZR, end='')