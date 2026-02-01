int(input())
s = {chr(i): i-64for i in range(65, 91)}
print(sum(s[e] for e in input()))