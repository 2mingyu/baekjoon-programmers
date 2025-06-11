R, C = map(int, input().split())
A, B = map(int, input().split())
for r in range(R):
    for a in range(A):
        s = '.' if r%2 else 'X'
        for c in range(C):
            for b in range(B):
                print(s, end='')
            s = '.' if s == 'X' else 'X'
        print()