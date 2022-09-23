# Find the kth smallest element in an array 
# https://practice.geeksforgeeks.org/problems/kth-smallest-element/0


def kth_smallest_element(arr, k):
    sorted_array = sorted(arr)
    print(sorted_array[k - 1])


lst = list(map(int, input().split()))
k = int(input())
kth_smallest_element(lst, k)