S = input()
l = []
i = len(S) - 1
while i >= 0:
    if S[i] == '0':
        l.append(10)
        i -= 2
    else:
        l.append(int(S[i]))
        i -= 1

print(f"{sum(l) / len(l):.2f}")
