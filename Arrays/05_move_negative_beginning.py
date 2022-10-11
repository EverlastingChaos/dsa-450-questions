# Move all the negative elements to one side of the array
# https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/


def shift_all(arr, left, right):
    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] > 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] > 0 and arr[right] > 0:
            right -= 1
        else:
            left += 1
            right -= 1


def display_arr(arr):
    for i in arr:
        print(i, end = " ")
    print()


if __name__ == '__main__':
    a = [-12, 11, -13, -5, 6, -7, 5, -3, 11]
    shift_all(a, 0, len(a) - 1)
    display_arr(a)

