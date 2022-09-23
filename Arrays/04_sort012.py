# Given an array which consists of only 0, 1 and 2. Sort without using any sorting algo
# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1


def sort012(arr):
    n = len(arr)
    count0 = 0
    count1 = 0
    count2 = 0
    
    for i in range(n):
        if arr[i] == 0:
            count0 += 1
        elif arr[i] == 1:
            count1 += 1
        else:
            count2 += 1

    index = 0
    while count0 > 0:
        arr[index] = 0
        count0 -= 1
        index += 1

    while count1 > 0:
        arr[index] = 1
        count1 -= 1
        index += 1

    while count2 > 0:
        arr[index] = 2
        count2 -= 1
        index += 1

    return arr


lst = list(map(int, input().split()))
print(sort012(lst))