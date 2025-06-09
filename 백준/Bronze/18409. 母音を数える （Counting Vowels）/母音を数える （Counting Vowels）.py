N = int(input())
S = input()
c = 0
for a in S:
    if a in 'aeiou': c += 1
print(c)