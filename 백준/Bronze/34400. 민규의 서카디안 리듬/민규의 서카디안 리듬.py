T = int(input())
for t in range(T):
    n = int(input())
    print(["OFFLINE", "ONLINE"][n%25 <17])