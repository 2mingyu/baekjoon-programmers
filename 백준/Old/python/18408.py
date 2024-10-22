"""
3 つの整数 (Three Integers)
111 = 3
112 = 4
122 = 5
222 = 6
print(sorted(input())[3])
"""
print('1122'[sum(map(int, input().split()))-3])