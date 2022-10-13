#

def find_longest_consq_subseq(arr, n):
    ans = 0
    s = set()

    for element in arr:
        s.add(element)

    for i in range(n):

        # check if curr element is start of the subseq
        if arr[i] - 1 not in s:

            # check for the next elements
            j = arr[i]
            while j in s:
                j += 1

            ans = max(ans, j - arr[i])
    
    return ans


arr = [1, 9, 3, 10, 4, 20, 2]
print(find_longest_consq_subseq(arr, len(arr)))
