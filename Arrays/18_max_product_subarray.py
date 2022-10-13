#

import sys


def get_max_product(arr, n):
    ans = -sys.maxsize - 1
    curr = 1
    last = 1
    for i in range(n):
        curr *= arr[i]
        last *= arr[n - i - 1]
        ans = max(ans, max(curr, last))
        if curr == 0:
            curr = 1
        if last == 0:
            last = 1
    return ans


arr = [2, 3, 4, 5, -1, 0]
print(get_max_product(arr, len(arr)))
