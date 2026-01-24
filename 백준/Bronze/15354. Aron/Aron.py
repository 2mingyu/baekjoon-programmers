N = int(input())
t = ''
r = 1
for _ in range(N):
    i = input()
    if i != t:
        r += 1
    t = i
print(r)