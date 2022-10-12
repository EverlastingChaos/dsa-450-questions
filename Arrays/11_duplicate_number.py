# find the duplicate number
# https://leetcode.com/problems/find-the-duplicate-number/


def get_duplicate_number(arr):
    arr.sort()
    duplicate_number = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == duplicate_number:
            return duplicate_number
        duplicate_number = arr[i]
    return -1

arr = [2,3,4,5,6,5]
print(get_duplicate_number(arr))