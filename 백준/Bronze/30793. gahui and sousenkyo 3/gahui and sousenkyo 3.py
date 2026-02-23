p, r = map(int, input().split())
if 5*p < r:
    print("weak")
elif 5*p < 2*r:
    print("normal")
elif 5*p < 3*r:
    print("strong")
else:
    print("very strong")