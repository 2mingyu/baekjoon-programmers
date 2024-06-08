"""
Bank Transfer
"""
k = int(input())
print("%.2f" % min(2000, max(100, k*0.01 + 25)))