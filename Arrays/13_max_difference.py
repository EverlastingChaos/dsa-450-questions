# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


def get_max_diff(arr, n):
    max_diff = arr[1] - arr[0]
    min_element = arr[0]
    for i in range(1, n):
        if arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element
        if arr[i] < min_element:
            min_element = arr[i]
    return max_diff


arr = [7, 1, 5, 3, 6, 4]
print(get_max_diff(arr, len(arr)))