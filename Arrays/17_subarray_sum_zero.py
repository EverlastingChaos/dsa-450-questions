# https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1


def zero_sum_exists(arr, n):
    n_sum = 0
    sum_set = set()
    for i in range(n):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in sum_set:
            return True
        sum_set.add(n_sum)
    return False


arr = [-3, 2, 3, 1, 6]
N = len(arr)
print(zero_sum_exists(arr, N))

