for _ in range(int(input())):
    S = input()
    print(min([S[i:] + S[:i] for i in range(len(S))]))