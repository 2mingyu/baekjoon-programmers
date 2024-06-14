"""
アイスクリーム (Ice Cream)
"""
S = int(input())
A = int(input())
B = int(input())
S = max(0, S-A)
print(250 + 100*(S//B + bool(S%B)))