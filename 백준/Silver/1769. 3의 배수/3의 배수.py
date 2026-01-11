X = list(input())
i = 0
while len(X) > 1:
    i += 1
    X = list(str(sum(map(int, X))))
print(i)
print(['NO', 'YES'][int(X[0])%3 == 0])