# https://leetcode.com/problems/merge-intervals/


def merge(intervals):
    intervals.sort()
    ans = [intervals[0]]
    for i in intervals:
        if i[0] <= ans[-1][1]:
            ans[-1][1] = max(i[1], ans[-1][1])
        else:
            ans.append(i)
    return ans


arr = [[1,3],[2,6],[8,10],[15,18]]
print(merge(arr))