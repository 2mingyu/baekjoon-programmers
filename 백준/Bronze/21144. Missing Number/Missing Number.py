n = int(input())
s = input()
i = 1
j = 0
while i <= n:
    l = len(str(i))
    if j+l <= len(s) and int(s[j:j+l]) == i:
        j += l
        i += 1
    else:
        print(i)
        break