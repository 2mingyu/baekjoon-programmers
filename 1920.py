"""
수 찾기
"""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0
import sys
input=sys.stdin.readline
input()
A=sorted(list(map(int,input().split())))
input()
for i in list(map(int,input().split())):print(binary_search(A,i))