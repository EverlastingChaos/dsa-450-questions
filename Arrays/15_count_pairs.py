# https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

from collections import defaultdict


def count_pairs(arr, n, k):
    # count = 0
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if arr[i] + arr[j] == k:
    #             count +=1
    # return count
        count = 0
        d = defaultdict(int)
        for i in arr:
            if k-i in d:
                count += d[k-i]
            d[i] += 1
            print(d)
        return count


arr = [1,2,3,4,4]
print(count_pairs(arr, len(arr), 5))
