n = int(input())
for _ in range(n):
    s = input()
    print(s + ('.' if s[-1] != '.' else ''))