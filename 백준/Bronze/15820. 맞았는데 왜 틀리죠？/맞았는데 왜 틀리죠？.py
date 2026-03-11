S1, S2 = map(int, input().split())
for _ in range(S1):
    a, b = map(int, input().split())
    if a != b:
        print('Wrong Answer')
        exit()
for _ in range(S2):
    a, b = map(int, input().split())
    if a != b:
        print('Why Wrong!!!')
        exit()
print('Accepted')