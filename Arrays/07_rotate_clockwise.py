# Given an array, rotate the array by one position in clock-wise direction.
# https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1


def rotate_clockwise(arr):
    arr[:] = arr[-1:] + arr[:-1]
    print(arr)


arr = [2, 4, 5, 7]
rotate_clockwise(arr)