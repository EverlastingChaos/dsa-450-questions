# Find the maximum and minimum element in an array
# link: https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/


def print_min_max(arr):
    sorted_array = sorted(arr)
    print(f"min: {sorted_array[0]}")
    print(f"max: {sorted_array[-1]}")


lst = list(map(int, input().split()))
print_min_max(lst)