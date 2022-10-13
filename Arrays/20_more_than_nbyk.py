#

def print_elements(arr, n, k):
    frequency = {}
    x = n // k

    for i in range(n):
        if arr[i] in frequency:
            frequency[arr[i]] += 1
        else:
            frequency[arr[i]] = 1

    for i in frequency:
        if frequency[i] > x:
            print(i)


arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
n = len(arr)
k = 4
print_elements(arr, n, k)
        