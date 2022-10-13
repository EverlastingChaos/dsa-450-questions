# https://practice.geeksforgeeks.org/problems/common-elements1132/1
# doesn't work with for eg: arr1 = arr2 = arr3 = [3,3,3]

import sys


def find_common_elements(arr1, n1, arr2, n2, arr3, n3):
    ans = []
    i, j, k = 0, 0, 0
    prev1 = prev2 = prev3 = -sys.maxsize - 1
    
    while i < n1 and j < n2 and k < n3:
        while arr1[i] == prev1 and i < n1 - 1:
            i += 1
        while arr2[j] == prev2 and j < n2 - 1:
            j += 1
        while arr3[k] == prev3 and k < n3 - 1:
            k += 1
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            ans.append(arr1[i])
            prev1 = arr1[i]
            prev2 = arr2[j]
            prev3 = arr3[k]
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            prev1 = arr1[i]
            i += 1
        elif arr2[j] < arr3[k]:
            prev2 = arr2[j]
            j += 1
        else:
            prev3 = arr3[k]
            k += 1
    return ans


arr1 = [3, 3, 3]
arr2 = [3, 3, 3]
arr3 = [3, 3, 3]
n1 = len(arr1)
n2 = len(arr2)
n3 = len(arr3)
print(find_common_elements(arr1, n1, arr2, n2, arr3, n3))

