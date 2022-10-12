def third_largest(arr):
    if len(arr) < 3:
        return "invalid input"

    first = arr[0]
    second = -999999
    third = -99999

    for i in range(1, len(arr)):
        if arr[i] > first:
            second = first
            third = second
            first = arr[i]
        elif arr[i] > second:
            third = second
            second = arr[i]
        elif arr[i] > third:
            third = arr[i]
    
    return third


arr = [12, 13, 1, 10, 34, 16]
print(third_largest(arr))
